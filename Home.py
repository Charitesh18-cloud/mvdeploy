import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="OCR App - Home", layout="centered")

# --- Title and Intro ---
st.title("📄 OCR Digitization App")
st.subheader("Extract text from images with ease!")

st.markdown("""
Welcome to your OCR-powered document digitization tool.

This app allows you to:
- 📤 Upload an image and extract text
- 💾 Save and view your documents
- 👤 Manage your profile
- ⚙ Customize your settings
""")

st.markdown("---")

# --- Navigation Buttons (inside main body) ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🖼 Upload Image"):
        st.switch_page("pages/1Upload.py")
    if st.button("💾 Saved Documents"):
        st.switch_page("pages/2SavedDocs.py")

with col2:
    if st.button("👤 Profile"):
        st.switch_page("pages/3Profile.py")
    if st.button("⚙ Settings"):
        st.switch_page("pages/4Settings.py")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤ using Streamlit and OCR API.")
