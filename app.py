import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Be My Valentine ❤️",
    page_icon="❤️",
    layout="centered"
)

# Read HTML file
html_file = Path("index.html")
html_content = html_file.read_text(encoding="utf-8")

# Render HTML
components.html(
    html_content,
    height=600,
    scrolling=False
)
