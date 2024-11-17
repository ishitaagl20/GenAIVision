# Image Describer, Object Finder, and Object Tracker

This project consists of three modules that utilize the **Gemini-1.5-Flash** model to analyze and interact with images and videos:

1. **Image Description**: Describes the contents of an uploaded image.
2. **Object Finder**: Finds the location of a specific object in an image.
3. **Object Tracker**: Tracks an object in a video and timestamps when the object appears.

---

## Modules

### 1. Image Description
- **Description**: Generates a textual description of the objects and scenes present in the uploaded image.
- **Input**: Image (JPG, JPEG, PNG)
- **Output**: A description of the objects and scenes in the image.

### 2. Object Finder
- **Description**: Locates a specified object (e.g., "pink wallet") in the uploaded image and provides its coordinates and description.
- **Input**:
  - Object name (e.g., "pink wallet")
  - Image (JPG, JPEG, PNG)
- **Output**: The location and description of the object in the image.

### 3. Object Tracker
- **Description**: Tracks a specified object in an uploaded video, taking snapshots every second and logging timestamps of when the object appears.
- **Input**:
  - Object name (e.g., "pink wallet")
  - Video file (MP4, AVI, etc.)
- **Output**: A list of timestamps when the object is detected, along with snapshots every second.

---

## Prerequisites

Before running the app, make sure you have the required Python libraries:

```bash
pip install streamlit pillow google-generativeai



