import streamlit as st
import streamlit.components.v1 as components

# 1. Page configuration
st.set_page_config(page_title="My Data Science Portfolio", layout="wide")

# 2. Perfect Full-Screen Hack (Streamlit ni black space hamesha mate hatavva)
st.markdown("""
    <style>
        /* Streamlit na vadhara na elements hide karva */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Iframe ne screen par exact 100% fit karva, jethi niche black space na vadhe */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
            z-index: 999999;
        }
        
        /* Streamlit (outer page) no scrollbar bandh karva */
        body { overflow: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Files read karo
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# 4. Scrollbar hide karvo pan scrolling chalu rakhvu (tamari requirement mujab)
hide_scrollbar_css = """
<style>
    /* Andar no jado scrollbar gayab karva */
    ::-webkit-scrollbar { display: none !important; }
    html, body { 
        -ms-overflow-style: none !important; 
        scrollbar-width: none !important; 
    }
</style>
"""

# 5. CSS, JS ane nava scrollbar logic ne HTML ma merge karo
html_code = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>\n{hide_scrollbar_css}')
html_code = html_code.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')

# 6. Streamlit iframe render karo
components.html(html_code)
