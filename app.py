import streamlit as st
import streamlit.components.v1 as components

# 1. Page settings
st.set_page_config(page_title="My Data Science Portfolio", layout="wide", initial_sidebar_state="collapsed")

# 2. Streamlit ni default jagya (padding) remove karva ane Iframe ne Full Screen (100vh) karva mate CSS
st.markdown("""
    <style>
        /* Streamlit ni aaju-baju ane upar-niche ni jagya kadhva mate */
        [data-testid="stAppViewBlockContainer"], .block-container, [data-testid="block-container"] {
            padding: 0px !important;
            max-width: 100% !important;
            margin: 0px !important;
        }
        
        /* Vadhara na Header ane Footer hide karva */
        header, footer {display: none !important; visibility: hidden !important;}
        
        /* Website ne exact Desktop Screen jetli size aape che (100vh), jethi last ma jagya na vadhe */
        iframe {
            height: 100vh !important;
            width: 100vw !important;
            border: none !important;
            margin: 0px !important;
            padding: 0px !important;
            display: block !important;
        }
        
        /* Main page no scrollbar gayab karva */
        ::-webkit-scrollbar { display: none !important; }
        body { -ms-overflow-style: none; scrollbar-width: none; overflow: hidden; }
    </style>
""", unsafe_allow_html=True)

# 3. HTML, CSS, JS read karo
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# 4. Andar no Scrollbar hide karva mate extra CSS (Scroll thase pan dekhase nahi)
hide_iframe_scrollbar = """
<style>
    ::-webkit-scrollbar { display: none !important; }
    html, body { -ms-overflow-style: none !important; scrollbar-width: none !important; margin: 0; padding: 0; }
</style>
"""

# 5. HTML ni andar CSS, JS ane Scrollbar hide nu CSS ek sathe jodi do
html_code = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>\n{hide_iframe_scrollbar}')
html_code = html_code.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')

# 6. Final code render karo (Height 100vh CSS thi force karyu che tethi ahiya height fixed nathi nakhvi padti)
components.html(html_code, height=800, scrolling=True)
