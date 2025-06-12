import streamlit as st

# Page configuration
st.set_page_config(page_title="OCR Home", layout="centered")

# Title
st.title("📄 OCR Powered Digitization")

# Welcome message
st.write("Welcome to the OCR Digitization App. Choose an action below:")

# Navigation using buttons (valid for multi-page apps)
if st.button("📤 Upload Image for OCR"):
    st.switch_page("pages/1Upload.py")

if st.button("📁 View Saved Documents"):
    st.switch_page("pages/2SavedDocs.py")

if st.button("👤 View Profile"):
    st.switch_page("pages/3Profile.py")

if st.button("⚙ App Settings"):
    st.switch_page("pages/4Settings.py")

# Streak/XP message
st.success("🟢 Streak and XP tracking will appear here soon!")