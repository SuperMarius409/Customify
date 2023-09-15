from pptx import Presentation
from bardapi import BardCookies
import streamlit as st
from streamlit_chat import message
import os

os.environ['HTTP_PROXY'] = 'http://10.11.4.1:3128'
os.environ['HTTPS_PROXY'] = 'http://10.11.4.1:3128'

st.title("The Powerfy")

def response_api(prompt):
    cookie_dict = {
        "__Secure-1PSID": "awi4iwZztiuw5Ce7U_0HS-MQ8dtI7zMInDnnIeDY8kpLcK7FZhKm4CqlujwZuRo5Ol9zbw.",
        "__Secure-1PSIDTS": "sidts-CjEBSAxbGf-b4mgEnqztimnmdCvE8gRf_y4vqOEGUqDngqgq0hLHleQLx_sQ_t0JSL1uEAA",
        "__Secure-1PSIDCC": "APoG2W8553fBEat_RRJJAoKJIvMuxUokDMnpLtGMrKC5v1hGb3ood_37ccfLiBlVChKYNDRpVw"
    }

    bard = BardCookies(cookie_dict=cookie_dict)

    message_response = bard.get_answer(str(prompt))['content']

    return message_response

def user_input():
    input_text = st.text_input("Enter your prompt: ")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state['generate'].append(output)
    st.session_state['generate'].append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        if i < len(st.session_state['past']):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        if i < len(st.session_state['generate']):
            message(st.session_state['generate'][i], key=str(i))
