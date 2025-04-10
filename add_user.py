import streamlit as st
from firebase import add_new_user

# page settings
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

### insert external css
def insert_css(css_file:str):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


# app container
app_column = st.columns([4,7,4],gap="small")

with app_column[1]:
    st.write("## 🤵 Add User")
    st.write("Enter email & password to create now 🤵user!")
    
    Email_input = st.text_input(
        label="Enter Email",
        type="default",
        key="email input"
    )

    Password_input = st.text_input(
        label="Enter Password",
        type="password",
        key="password input"
    )

    add_user_btn = st.button(label="Add User🤵", key="add user")

    if add_user_btn:
        if Email_input.strip() != "" and Password_input.strip() != "":
                add_new_user(email_id=Email_input,password=Password_input)
        else:
            st.warning("Fill all input fields !",icon="⚠️")


insert_css("css_files/app.css")