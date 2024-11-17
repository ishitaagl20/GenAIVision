import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure the Gemini Vision model
genai.configure(api_key="")

# Function to generate an image description
def describe_image(image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure correct model identifier
    default_prompt = "Describe the content of this image."
    response = model.generate_content([default_prompt, image])
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Image Describer", layout="wide")
st.title("🖼️ Image Describer")
st.write("Upload an image, and the AI will provide a description of its content.")

# File Uploader
uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG):", type=["jpg", "jpeg", "png"])

# Display Image and Description
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Describe Image"):
        st.info("Analyzing the image, please wait...")
        try:
            response = describe_image(image)
            st.success("Image Description:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload an image to get its description.")
