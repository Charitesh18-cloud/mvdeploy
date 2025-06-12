# pages/2_SavedDocs.py
import streamlit as st
import base64

def download_text(text, filename="document.txt"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download Export</a>'
    return href

st.title("📚 Saved OCR Documents")

if "saved_docs" not in st.session_state or not st.session_state.saved_docs:
    st.info("No documents saved yet.")
else:
    for i, doc in enumerate(st.session_state.saved_docs):
        st.subheader(f"Document {i+1}")
        st.code(doc)
        st.markdown(download_text(doc, f"document_{i+1}.txt"), unsafe_allow_html=True)