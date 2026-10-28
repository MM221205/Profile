import streamlit as st
import streamlit.components.v1 as components

# 1. Page ne wide mode ma set karo
st.set_page_config(page_title="My Data Science Portfolio", layout="wide")

# 2. Charey baju ni jagya (padding) remove karva custom CSS
st.markdown("""
    <style>
        .appview-container .main .block-container {
            padding-top: 0rem;
            padding-right: 0rem;
            padding-left: 0rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. HTML, CSS, ane JS files read karo
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# 4. HTML ni andar CSS ane JS inject karo
html_code = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>')
html_code = html_code.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')

# 5. Render karo (Height 2000 rakhi che jethi andar no alag scrollbar na aave)
components.html(html_code, height=2000, scrolling=True)
