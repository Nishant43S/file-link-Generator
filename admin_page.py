import streamlit as st
from firebase import *
from firebase_admin import credentials, auth
import firebase_admin
import random


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
                    st.subheader("All Users")
                    st.dataframe(Get_all_Users(),use_container_width=True)
                
                # delete users
                if Remove_user_email:
                    st.subheader("Remove Users")
                    st.write("")
                    # st.write("")
                    Remove_users()
                
                if Create_Verified_user:
                    st.subheader("Create Verified Users")
                    Email_input_variefication = st.text_input(
                        label="Enter Email",
                        type="default",
                        key="email vaerification input"
                    )
                    if st.button(" 👩‍💻 Verify User",key="verify btn"):
                        with st.spinner("Generating Link..."):
                            Create_varified_user(str(Email_input_variefication))
                        
                

        else:
            st.warning("Fill all credentials!",icon="⚠️")


insert_css("css_files/app.css")