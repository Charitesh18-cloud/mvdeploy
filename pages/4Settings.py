# pages/4_Settings.py
import streamlit as st

st.title("⚙ Settings")

st.checkbox("🌙 Dark Mode (System default)")
st.selectbox("🔤 App Language", ["English", "Telugu", "Hindi"])
st.checkbox("🔔 Enable Notifications")
st.text_input("Change Display Name")

if st.button("Reset Progress"):
    st.session_state.xp = 0
    st.session_state.streak = 1
    st.session_state.saved_docs = []
    st.success("Progress reset!")