# pages/1_Upload.py
import streamlit as st
import pytesseract
from PIL import Image

st.title("📤 Upload and Extract Text")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    text = pytesseract.image_to_string(image)
    st.text_area("Extracted Text", text, height=200)

    if "saved_docs" not in st.session_state:
        st.session_state.saved_docs = []
    if "xp" not in st.session_state:
        st.session_state.xp = 0

    if st.button("Save Document"):
        st.session_state.saved_docs.append(text)
        st.session_state.xp += 10
        st.success("Document saved! XP +10")