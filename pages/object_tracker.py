import streamlit as st
import cv2
from PIL import Image, PngImagePlugin
import google.generativeai as genai
import tempfile
import os

# Configure the Gemini Vision model
genai.configure(api_key="")

# Function to load Gemini Vision model and get object detection response
def get_object_details(object_name, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure correct model identifier
    # Create a default prompt if no object is specified
    default_prompt = "Identify all objects in the image."
    prompt = f"Find the '{object_name}' in the image. Say OBJECT FOUND if the object is present and Give the location of the object and Describe anything relevant to it" if object_name else default_prompt
    response = model.generate_content([prompt, image])
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Object Tracker", layout="wide")
st.title("📷 Object Tracker")
st.write(
    "Upload a video and specify an object to find. The AI will process the video and give a timestamp when the object is found."
)

# User Inputs
object_name = st.text_input(
    "Enter the name of the object to find:",
    placeholder="e.g., 'pink wallet'",
    key="object_name",
)

uploaded_video = st.file_uploader("Upload a video (MP4, AVI, MOV):", type=["mp4", "avi", "mov"])

# Display Video (if uploaded)
if uploaded_video is not None:
    st.video(uploaded_video)

# Function to process the video and detect the object
def process_video(video_file, object_name):
    # Create a temporary file to store uploaded video
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(video_file.read())
        video_path = temp_file.name

    # Open the video using OpenCV
    cap = cv2.VideoCapture(video_path)

    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    timestamp_list = []  # To store timestamps when the object is found

    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Capture frame every 1 second
        if frame_num % int(frame_rate) == 0:
            # Convert the frame to PIL Image for processing
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Call the AI model to detect the object
            response = get_object_details(object_name, pil_image)

            # Check if the object is detected and log the timestamp
            if "object found" in response.lower():  # Modify condition based on actual response format
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Convert to seconds
                timestamp_list.append(f"Object found at {timestamp:.2f} seconds")
        
        frame_num += 1
    
    cap.release()
    os.remove(video_path)  # Clean up the temporary file
    
    return timestamp_list

# Submit Button
if st.button("Process Video"):
    if uploaded_video is not None and object_name:
        st.info("Processing the video, please wait...")
        try:
            timestamps = process_video(uploaded_video, object_name)
            if timestamps:
                st.success("Object Detection Timestamps:")
                for timestamp in timestamps:
                    st.write(timestamp)
            else:
                st.warning("No object detected in the video.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload a video and specify an object name.")
