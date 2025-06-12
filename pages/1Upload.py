import streamlit as st
import requests
from PIL import Image
import io

OCR_API_KEY = "K81027426088957"  # Replace with your key

def ocr_space_file(image_file):
    url = 'https://api.ocr.space/parse/image'
    image_bytes = image_file.read()
    response = requests.post(
        url,
        files={'filename': image_bytes},
        data={
            'apikey': OCR_API_KEY,
            'language': 'eng',
        },
    )
    result = response.json()
    if result.get("IsErroredOnProcessing"):
        return "Error: " + result.get("ErrorMessage", ["Unknown error"])[0]
    return result["ParsedResults"][0]["ParsedText"]

def app():
    st.title("Upload and Extract Text")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Extracting text..."):
            text = ocr_space_file(uploaded_image)
        st.text_area("Extracted Text", text, height=300)
