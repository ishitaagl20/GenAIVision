import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Vision Tools", layout="centered")

# Add title and description
st.title("🌟 AI Vision Tools")
st.write("Welcome to AI Vision Tools! Choose a module to get started.")

# Links to internal pages
st.page_link("pages\image_describer.py", label="Image Describer",  icon="1️⃣")
st.page_link("pages\object_finder.py", label="Object Finder",icon="2️⃣")
st.page_link("pages\object_tracker.py", label="Object Tracker", icon="3️⃣")

# Optional: External link
st.page_link("https://www.https://gemini.google.com/app", label="Build Using Gemini", icon="🌍")
