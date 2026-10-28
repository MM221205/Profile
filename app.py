import streamlit as st
import streamlit.components.v1 as components

# Page layout set karva
st.set_page_config(page_title="Mahek"s Profile", layout="wide")

# Files read karvi
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# HTML ni andar CSS ane JS inject karva
html_code = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>')
html_code = html_code.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')

# Streamlit ma render karvu
components.html(html_code, height=1200, scrolling=True)
