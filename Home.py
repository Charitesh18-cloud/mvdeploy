import streamlit as st
import pytesseract
from PIL import Image
import numpy as np
import cv2

# Page configuration
st.set_page_config(page_title="OCR Home", layout="centered")

# Sidebar Navigation
st.sidebar.title("📚 Navigation")
st.sidebar.page_link("Home.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/1Upload.py", label="🖼 Upload Image")
st.sidebar.page_link("pages/2SavedDocs.py", label="💾 Saved Documents")
st.sidebar.page_link("pages/3Profile.py", label="👤 Profile")
st.sidebar.page_link("pages/4Settings.py", label="⚙ Settings")

# Main Title
st.title("📄 OCR Digitization App")
st.caption("Convert images to editable text using Tesseract OCR.")

# Upload Section
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # Convert to OpenCV format for OCR
    img_np = np.array(image)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # OCR Extraction
    extracted_text = pytesseract.image_to_string(img_cv)

    # Display Text
    st.subheader("🔍 Extracted Text")
    st.text_area("Result", extracted_text, height=200)

    # Download Button
    st.download_button("💾 Download as .txt", extracted_text, file_name="extracted_text.txt")

else:
    st.info("Upload an image above to extract text.")

# Footer
st.markdown("---")
st.markdown("Built with ❤ using Streamlit and Tesseract OCR.")
