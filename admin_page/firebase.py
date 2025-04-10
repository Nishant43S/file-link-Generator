import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
import json
import streamlit as st
import uuid


# # Initialize Firebase Admin SDK

app_name = "firebase app {}".format(str(uuid.uuid4()))


cred = credentials.Certificate("firebase_app/key.json")
firebase_admin.initialize_app(cred)

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

        st.write(f"Verification link - {verification_link}")
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