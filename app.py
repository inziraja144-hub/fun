import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Be My Valentine ❤️",
    page_icon="❤️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
}
.box {
    background: rgba(0,0,0,0.25);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
}
.title {
    color: white;
    font-size: 40px;
}
.msg {
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Center container
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<div class="title">Will you be my Valentine? ❤️</div>', unsafe_allow_html=True)
st.write("")

# Session state
if "answered" not in st.session_state:
    st.session_state.answered = False

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES ❤️"):
        st.session_state.answered = True

with col2:
    st.button("NO 😅")

# Message
if st.session_state.answered:
    st.markdown(
        '<div class="msg">Yayyy ❤️ Best decision ever. Love you!</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
