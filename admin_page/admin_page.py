import streamlit as st
from firebase import *
from firebase_admin import credentials, auth
import firebase_admin
import pyrebase
import json
import random
import humanize


# page settings
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

### insert external css
def insert_css(css_file:str):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)



app_sidebar = st.sidebar

with app_sidebar:
    Display_all_user = st.checkbox(
        label="Get all users",
        key="all users",
        value=True
    )

    Remove_user_email = st.checkbox(
        label="Delete users",
        key="delete users",
        value=True
    )

    Create_Verified_user = st.checkbox(
        label="Create Verified users",
        key="Create Verified  users",
        value=False
    )

    Reset_user_password = st.checkbox(
        label="Reset Email password",
        key="reset pass",
        value=False
    )

    Dropbox_files = st.checkbox(
        label="Manage dropbox",
        key="dropbox",
        value=False
    )

app_column = st.columns([4,7,4],gap="small")

with app_column[1]:
    st.write("## 📑File Link Generator - Admin Panel")

    
    Email_input = st.text_input(
        label="Enter verified Email",
        type="default",
        key="email input"
    )

    Password_input = st.text_input(
        label="Enter Password",
        type="password",
        key="password input"
    )

    LogedIn_btn = st.toggle(label="📧 Admin LogIn", key="login user")

    if LogedIn_btn:
        if Email_input.strip() != "" and Password_input.strip() != "":
            login_user(
                email_id=Email_input,
                password=Password_input
            )

            # check user is variefied
            verified = is_email_verified(Email_input, Password_input)

            if verified is False:
                st.warning(f"The email {Email_input} is NOT verified \n use verified email!",icon='⚠️')

            elif verified is True:
                st.sidebar.success(f"Verified Email \n\n {Email_input}")
                st.markdown(
                    "<h2 style='color: orangered;'>Admin Panel</h2>",
                    unsafe_allow_html=True
                )

                # display users
                if Display_all_user:
                    st.subheader("🙎 All Users")
                    st.dataframe(Get_all_Users(),use_container_width=True)
                
                # delete users
                if Remove_user_email:
                    st.subheader("Remove Users")
                    st.write("")
                    # st.write("")
                    Remove_users()
                
                # verified user
                if Create_Verified_user:
                    st.subheader("✅ Create Verified Users")
                    Email_input_variefication = st.text_input(
                        label="Enter Email",
                        type="default",
                        key="email vaerification input"
                    )
                    if st.button(" 👩‍💻 Verify User",key="verify btn"):
                        with st.spinner("Generating Link..."):
                            Create_varified_user(str(Email_input_variefication))
                            
                # reset password
                if Reset_user_password:
                    st.subheader("🔐 Reset Password")
                    Email_input_reset = st.text_input(
                        label="Enter Email",
                        type="default",
                        key="email password reset"
                    )
                    if st.button(" 👩‍💻 Reset Password",key="reset btn"):
                        with st.spinner("Generating Link..."):
                            Reset_password(str(Email_input_reset))
                
                if Dropbox_files:
                    st.subheader("📁 Dropbox File Manager")

                    # input of token
                    token = st.text_input("🔑 Enter your Dropbox Access Token", type="password")
                    

                    if token:
                        try:
                            dbx = validate_token(token)
                            if dbx:
                                st.success("🔓 Access token is valid.")
                                # Show file list
                                files = list_files(dbx)
                                if files:
                                    st.subheader("📄 Files in Dropbox")
                                    file_data = []
                                    for file in files:
                                        if isinstance(file, dropbox.files.FileMetadata):
                                            file_data.append({
                                                "Name": file.name,
                                                "Size": humanize.naturalsize(file.size),
                                                "Path": file.path_display,
                                            })

                                    st.table(file_data)
                                
                                # Button to delete all files
                                
                                token_input = token

                                if st.button("🚨 Delete All Dropbox Files"):
                                    if token_input.strip() == "":
                                        st.warning("Please enter a valid access token.")
                                    else:
                                        with st.spinner("Deleting files..."):
                                            result = delete_all_dropbox_files(token_input)
                                        st.success("files deleted")
                            else:
                                st.info("No files found in your Dropbox.")
                        except:
                            st.warning("❌ Invalid access token. Please try again.")

        else:
            st.warning("Fill all credentials!",icon="⚠️")


insert_css("css_files/app.css")