''' Restaurant AI'''

from bardapi import Bard
import streamlit as st
from streamlit_chat import message
import os
#hi

os.environ["_BARD_API_KEY"] = 'cQhm5m2CXx0CmB56MqgG2FUbEe3sLz2frDhY33Cq2D-W5rJKxyFUBhPsD2gDjc49i8LZBw.'


# message = input('Enter Your prompt : ')
# print(Bard().get_answer(str(message))['content'])

st.title("Restaurant AI")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Prompt : ")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)


if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])- 1, -1, -1):
        message(st.session_state['generate'][i], is_user=True, key=str(i)+'_user')
        message(st.session_state['past'][i], key=str(i))
