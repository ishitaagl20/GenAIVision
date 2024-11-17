import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure the Gemini Vision model
genai.configure(api_key="")

# Function to load Gemini Vision model and get object detection response
def get_object_details(object_name, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure correct model identifier
    # Create a default prompt if no object is specified
    default_prompt = "Identify all objects in the image."
    prompt = f"Find the '{object_name}' in the image. Give the location of the object and Describe anything relevant to it" if object_name else default_prompt
    response = model.generate_content([prompt, image])
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Object Finder", layout="wide")
st.title("🔍 Object Finder")
st.write(
    "Upload an image and specify an object to find. If no object is specified, the AI will identify all objects in the image."
)

# User Inputs
object_name = st.text_input(
    "Enter the name of the object to find:",
    placeholder="e.g., 'A pink wallet'",
    key="object_name",
)

uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG):", type=["jpg", "jpeg", "png"])

# Display Uploaded Image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    st.warning("Please upload an image to proceed.")

# Submit Button
if st.button("Identify Objects"):
    if uploaded_file is not None:
        st.info("Analyzing the image, please wait...")
        try:
            response = get_object_details(object_name, image)
            st.success("Analysis Complete:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("No image uploaded. Please upload an image and try again.")
