import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
import json
import streamlit as st
import uuid
import dropbox
from dropbox.exceptions import AuthError
import humanize
import random



# Function to validate token
def validate_token(token):
    try:
        dbx = dropbox.Dropbox(token)
        dbx.users_get_current_account()
        return dbx
    except AuthError:
        return None

# Get file list
def list_files(dbx):
    try:
        response = dbx.files_list_folder(path="")
        files = response.entries
        while response.has_more:
            response = dbx.files_list_folder_continue(response.cursor)
            files.extend(response.entries)
        return files
    except Exception as e:
        st.error(f"Error listing files: {e}")
        return []
def delete_all_dropbox_files(access_token: str) -> str:
    try:
        dbx = dropbox.Dropbox(access_token)
        deleted_files = []

        # List all files/folders in root recursively
        result = dbx.files_list_folder(path="", recursive=True)
        entries = result.entries

        while result.has_more:
            result = dbx.files_list_folder_continue(result.cursor)
            entries.extend(result.entries)

        for entry in entries:
            dbx.files_delete_v2(entry.path_lower)
            deleted_files.append(entry.path_display)

        if deleted_files:
            return f"✅ Deleted {len(deleted_files)} files/folders:\n" + "\n".join(deleted_files)
        else:
            return "✅ No files or folders to delete."

    except dropbox.exceptions.AuthError:
        return "❌ Invalid access token."
    except dropbox.exceptions.ApiError as api_err:
        return f"❌ API Error: {api_err.user_message_text or str(api_err)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# # Initialize Firebase Admin SDK


def firebase_app(app_name):
    cred = credentials.Certificate("firebase_app/key.json")
    firebase_admin.initialize_app(cred,
    name=f"{app_name} - {random.randint(1000,10000)}"
    )

def read_cred(file_path):
    """Reads a JSON file config"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return None
    
firebaseConfig = read_cred("firebase_app/cred.json")

firebase = pyrebase.initialize_app(firebaseConfig)
login_auth = firebase.auth()


# add user
def add_new_user(email_id,password):
    try:
        login_auth.create_user_with_email_and_password(email=email_id,password=password)
        st.success(f"user - {email_id} Created.")
    except Exception as e:
        return st.warning("Error... \n {}".format("Email already exists"),icon="⚠️")
    
# login user
def login_user(email_id,password):
    try:
        login_auth.sign_in_with_email_and_password(email=email_id,password=password)
        st.toast("User loged in",icon="📩")
    except :
        return st.warning("Error... \n {}".format("invalid credentials"),icon="⚠️")
    
#
def is_email_verified(email, password):
    try:
        # Sign in the user
        user = login_auth.sign_in_with_email_and_password(email, password)
        
        # Get account info
        account_info = login_auth.get_account_info(user['idToken'])
        verified = account_info['users'][0]['emailVerified']
        
        return verified
    except Exception as e:
        print("Error:", e)
        return None

# create verified user
def Create_varified_user(Email_id):
    try:
        verification_link = auth.generate_email_verification_link(Email_id)

        st.markdown(
            f"verification Link - <a href='{verification_link}' target='_blank'>Click To verify</a>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"error... {e}")

# get all users
def Get_all_Users():
    email_id = []
    user_id = []
    page = auth.list_users()
    for i in page.users:
        email_id.append(i.email)
        user_id.append(i.uid)
    page.get_next_page()
    return {
        "Email Id":email_id,
        "User Id":user_id
    }


### remove users

def delete_user_by_uid(uid):
    try:
        auth.delete_user(uid)
        st.toast(f"Successfully deleted: {uid}")
    except auth.AuthError as e:
        st.error(f"error {e}")

#check verified
def check_user_verified(email):
    try:
        user = auth.get_user_by_email(email)
        if user.email_verified:
            st.markdown(f"<p style='color: palegreen;'>✅ User {email} is verified.</p>",
                        unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: red;'>❌ User {email} is NOT verified.</p>",
                        unsafe_allow_html=True)
    except auth.UserNotFoundError:
        print("User not found.")

# delete users
def Remove_users():
    page = auth.list_users()
    for i in page.users:
        st.write(f"Email Id - {i.email}")
        st.write(f"User Id - {i.uid}")
        check_user_verified(i.email)
        email_delete = lambda x: x.split("@")[0]
        if st.button(label=f"Delete {email_delete(i.email)}.",key=i.uid):
            delete_user_by_uid(i.uid)
        st.write("---")
    page.get_next_page()

def Reset_password(Email_id):
    try:
        reset_link = auth.generate_password_reset_link(Email_id)
        return reset_link
    except Exception as e:
        st.warning(f"Error... {e}",icon="⚠️")