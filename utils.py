from google import genai
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st
import os

load_dotenv()

def memory():
    """
    Makes the empty session state for the response.

    Arguments
    ---------
    None

    Returns
    ----------
    st.session_state: Session state of streamlit
    """
    if "landmark_name" not in st.session_state:
        st.session_state["landmark_name"] = None
    
    if "landmark_details" not in st.session_state:
        st.session_state["landmark_details"] = None

    if "hist_fact" not in st.session_state:
        st.session_state["hist_fact"] = None

    if "near_place" not in st.session_state:
        st.session_state["near_place"] = None

    if "trip_advice" not in st.session_state:
        st.session_state["trip_advice"] = None
    
    return st.session_state


#  Get the API key from enviromnent
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# google gemini llm
client = genai.Client(api_key= os.environ["GOOGLE_API_KEY"])


# chatgroq gemma llm
llm = ChatGroq(
    model = "gemma2-9b-it",
    temperature = 0
)

def make_chain(prompt):
    """
    Function to make the chain using llm and prompt.
    Takes prompt and make the chain and returns the chain.

    Arguments
    ---------
    prompt : The text that will goes to the llm.

    Returns
    ---------
    chain : QA chain for generating the response.
    """

    prompt_temp = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("human", "{landmark_name}")
        ]
    )

    chain = prompt_temp | llm | StrOutputParser()

    return chain

def make_chain_for_json(prompt):

    prompt_temp = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("human", "{landmark_name}")
        ]
    )

    chain = prompt_temp | llm | JsonOutputParser()

    return chain