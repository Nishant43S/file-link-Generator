import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

### insert external css
def insert_css(css_file:str):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# app settings css
insert_css("css_files/app.css")

# ### insert external html file
def insert_html(html_file):
    with open(html_file) as f:
        return f.read()
# app container
app_column = st.columns([4,7,4],gap="small")

with app_column[1]:
    st.markdown(insert_html("html_file/about.html")
                ,unsafe_allow_html=True)