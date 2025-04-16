from utils import client 
from prompt import image_detection_prompt, text_checker_prompt
import streamlit as st

def detect_landmark(image):
    """
    Function to detect the landmark from image.
    Takes the image as argument give it to the model and predict the landmark.

    Arguement
    ---------
    image : Image of landmark.

    Returns
    --------
    img_response.text : Returns the name of landmark

    """
    try:
        img_response = client.models.generate_content(
            model = "gemini-2.0-flash",
            contents= [image_detection_prompt, image] 
        )
        return img_response.text
    
    except:
        st.error("Please check your internet connection !!!!", icon = "🔌")

def detect_landmark_text(text):
    """
    Function to detect the landmark from text.
    Takes the text as argument give it to the model and detect  the landmark with spelling correction.

    Arguement
    ---------
    image : Image of landmark.

    Returns
    --------
    img_response.text : Returns the name of  landmark with spelling correction.
    """
    try:
        img_response = client.models.generate_content(
            model = "gemini-2.0-flash",
            contents= [text_checker_prompt, text] 
        )
        return img_response.text

    except:
        st.error("Please check your internet connection !!!!", icon = "🔌")


