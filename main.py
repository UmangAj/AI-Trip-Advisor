import streamlit as st
from landmark_detection import detect_landmark, detect_landmark_text
from PIL import Image
from utils import memory, make_chain, make_chain_for_json
from prompt import landmark_details_prompt, landmark_hist_prompt, landmark_trip_prompt, landmark_near_place_prompt
from fetch_image import get_image

def get_places_url(data):
    """
    Function to add image url into near places session state key.

    Arguments
    ---------
    data : value of session state's near by place

    Returns
    new data with image url
    """
    for item in data:
        item['image_url'] = get_image(item['place_name'],1)[0]
    return data

def sidebar_func():
    """
    Function to add sidebar.
    Contains the Upload image.
    Insert text.
    About section of applications.

    Arguments
    ---------
    None

    Returns
    ---------
    None
    """

    #choose the option for input image or text.
    st.sidebar.write("### Search Option")
    user_selection =  st.sidebar.radio(" ", ["Enter Image", "Enter Text"], label_visibility = "collapsed")

    #if input is image.
    predicted_landmark_name = None
    if user_selection == "Enter Image":
        st.sidebar.write("### Enter Your Image")
        uploaded_image = st.sidebar.file_uploader("None", type = ["jpg", "jpeg", "png"], label_visibility = "collapsed")

        if uploaded_image:
            landmark_image = Image.open(uploaded_image)

            predicted_landmark_name = detect_landmark(landmark_image)

            #if any other images are uploaded
            if predicted_landmark_name == '1':
                st.warning(" Please enter only landmark image.", icon = '⚠️')

    #if input is text.
    elif user_selection == "Enter Text":

        st.sidebar.write("### Enter Your Text")
        landmark_name = st.sidebar.text_input("None", label_visibility = "collapsed")

        if landmark_name:
            temp_landmark_name = detect_landmark_text(landmark_name)
            try:
                # if text not contains the landmark name
                temp_landmark_name = int(temp_landmark_name)
                
                if temp_landmark_name == 1:
                    st.warning(" Please enter only landmark name.", icon = '⚠️')

            except ValueError:
                predicted_landmark_name = temp_landmark_name
    
    st.sidebar.divider()
    st.sidebar.write("### About")
    st.sidebar.markdown("<p style='text-align: justify'> This AI-powered tool identifies landmarks from uploaded images or user-input text, providing key details, historical facts, nearby attractions, and travel advice.</p>", unsafe_allow_html=True)

    return predicted_landmark_name
            
# streamlit UI
st.set_page_config(page_icon = "🧳", page_title = "AI Trip Advisor")

st.markdown("<h1 style='text-align: center;'>AI Trip Advisor 🧳</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Explore Like Never Before: AI-Powered Travel Adventures.</h5>", unsafe_allow_html=True)

font_css = """
<style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    font-size: 19px
    }
    div[data-baseweb="tab-list"]{
    justify-content: center;
    align-item: center;
    gap: 30px;
    margin-top: 18px}
</style>
"""
st.write(font_css, unsafe_allow_html=True)

# adding data into memory
try:
    session_state = memory()
    landmark_details_chain = make_chain(landmark_details_prompt)
    landmark_hist_chain = make_chain(landmark_hist_prompt)
    landmark_trip_chain = make_chain(landmark_trip_prompt)
    landmark_near_place_chain = make_chain_for_json(landmark_near_place_prompt)

except:
    st.error("Please check your internet connection !!!!", icon = "🔌")

predicted_landmark_name = sidebar_func()

if predicted_landmark_name != '1' and predicted_landmark_name:

    with st.spinner("Fetching details..."):

        session_state['landmark_name'] = predicted_landmark_name
        session_state['landmark_details'] = landmark_details_chain.invoke(predicted_landmark_name)
        session_state['hist_fact'] = landmark_hist_chain.invoke(predicted_landmark_name)
        session_state['trip_advice'] = landmark_trip_chain.invoke(predicted_landmark_name)
        session_state['near_place'] = landmark_near_place_chain.invoke(predicted_landmark_name)
        data = get_places_url(session_state['near_place'])
        session_state['near_place'] = data
        tab1, tab2, tab3, tab4 = st.tabs(["Details", "Historical Facts", "Near by Places", "Trip Advice"])

    with tab1:
        st.markdown(session_state["landmark_details"])

    with tab2:
        st.markdown(session_state["hist_fact"])

    with tab3:

        for i in session_state["near_place"]:
            
            st.markdown(f"#### {i['place_name']}")
            col1, col2 = st.columns(2, border=True)
            with col1:
                st.image(i["image_url"], use_container_width=True)
            with col2:
                st.markdown(f"<p style='text-align: justify; font-size: 17px'> {i['description']} </p>", unsafe_allow_html=True)

    with tab4:
        st.markdown(session_state["trip_advice"])

    




