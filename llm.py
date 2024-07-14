import os
import cohere
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.environ.get("COHERE_FREE_API"))

def stream_chat(instruction, data):
    cohere_response = co.chat_stream(message=f"{instruction} \n {data}",
                                     temperature=0.2,
                                    chat_history = None,
                                     model="command-r-plus")

    for event in cohere_response:
        if event.event_type == "text-generation":
            st.session_state.notes += event.text
            yield event.text

def non_stream_chat(instruction, data):
    """
    This function sends a non-streaming chat request to the Cohere API.

    Parameters:
    instruction (str): The instruction or command to be given to the AI model.
    data (str): The data or context to be used in the chat.

    Returns:
    str: The response from the Cohere API.

    Note:
    This function uses the Cohere API's chat method with a temperature of 0.7 and the "command-r-plus" model.
    """
    cohere_response = co.chat(message=f"{instruction} \n {data}",
                              temperature=0.7,
                              chat_history = None,
                              model="command-r-plus")
    return cohere_response.text