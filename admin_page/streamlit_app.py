import streamlit as st
from firebase import *


### page setup

admin_page = st.Page(
    page="admin_page.py",
    title="Admin Page",
    icon=":material/globe:",
    default=True
)

add_user = st.Page(
    page="add_user.py",
    title="Add User",
    icon=":material/description:",
)


about_app = st.Page(
    page="about_app.py",
    title="About App",
    icon=":material/person:"
)



page = st.navigation(
    pages=[admin_page,add_user,about_app],
    expanded=False,position="sidebar"
)

page.run()

app_sidebar = st.sidebar

with app_sidebar:
    name_of_app = st.text_input(
        label="app name",key='app name'
    )
    firebase_app(name_of_app)
    # project Link
    st.link_button(
        label="Project Link",
        url="https://github.com/Nishant43S/file-link-Generator.git",
        icon=":material/code_off:",
        use_container_width=True
    )
    st.write("Developed by - Nishant Maity")