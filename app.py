import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Be My Valentine ❤️",
    page_icon="❤️",
    layout="centered"
)

# Absolute path to current directory
BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "index.html"

if not HTML_FILE.exists():
    st.error("❌ index.html not found. Make sure it is in the same folder as app.py")
else:
    html_content = HTML_FILE.read_text(encoding="utf-8")
    components.html(html_content, height=650, scrolling=False)
