import streamlit as st
import streamlit.components.v1 as components

# 1. Page settings
st.set_page_config(page_title="My Data Science Portfolio", layout="wide", initial_sidebar_state="collapsed")

# 2. Perfect CSS: Streamlit nu scrolling LOCK karva ane Black Space hatavva mate
st.markdown("""
    <style>
        /* Aaju-baju ni badhi padding/margin zero karvi */
        .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        
        /* Header ane Footer hide karva */
        header, footer, #MainMenu {visibility: hidden !important; display: none !important;}
        
        /* SAOTHI JARURI: Streamlit na bahar na page nu scrolling bandh (lock) karvu */
        [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] > .main {
            overflow: hidden !important;
            background-color: #0b1020 !important; /* Tamara portfolio jevo j same color */
        }
        
        /* Iframe ne aakhi desktop screen par lock karvu */
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 999999 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. HTML, CSS, JS Files read karo
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# 4. Tamari app (iframe) ni andar no scrollbar hide karvo
hide_inner_scrollbar = """
<style>
    /* Scrollbar ni patti hide thase pan scrolling aaram thi thase */
    ::-webkit-scrollbar { display: none !important; }
    body, html { -ms-overflow-style: none !important; scrollbar-width: none !important; }
</style>
"""

# 5. HTML ni andar CSS ane JS add karo
html_code = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>\n{hide_inner_scrollbar}')
html_code = html_code.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')

# 6. Render karo
components.html(html_code, height=800)
