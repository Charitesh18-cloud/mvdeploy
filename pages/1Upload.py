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

# --- Page Settings ---
st.set_page_config(page_title="Upload & OCR", layout="centered")

# --- UI Content ---
st.title("ðŸ–¼ Upload Image for OCR")
st.caption("Convert your images to text using OCR Space API")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Extracting text..."):
        extracted_text = ocr_space_file(uploaded_image)

    st.subheader("ðŸ” Extracted Text")
    st.text_area("Result", extracted_text, height=300)

    # Export Text Button
    st.download_button(
        label="ðŸ’¾ Download Text",
        data=extracted_text,
        file_name="ocr_output.txt",
        mime="text/plain"
    )
else:
    st.info("Please upload an image to begin text extraction.")
