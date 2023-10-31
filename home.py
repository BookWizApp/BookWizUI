import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import requests
flask_app_url1 = 'http://5ef5-34-125-141-135.ngrok-free.app'
flask_app_url2 = 'http://7350-34-125-5-73.ngrok-free.app'
def summarizing(data):
    response = requests.post(f'{flask_app_url1}/get_summary', json=data)
    print(response)
    summary = response.json().get('summary')
    st.write(f"Summary: {summary}")
def questionAnswering(data):  
    response = requests.post(f'{flask_app_url2}/get_answer', json=data)
    print(response)
    answer = response.json().get('answer')
    st.write(f"Answer: {answer}")
def app():
    st.title("Welcome to Summary & QA Session")
    if st.session_state.username=='':
        buttonval = 'Create Account or Login'
        #ph = 'Login to be able to post!!'
    else:
        buttonval = 'Select a Book'
        #ph='Post your thought'    
    #post=st.text_area(label=' :orange[+ New Post]',placeholder=ph,height=None, max_chars=500)
    if buttonval == 'Create Account or Login':
        st.button('Creat Account or Login', key='switch_button')
            # st.markdown('<a href="/next_page" target="_self">Next page</a>', unsafe_allow_html=True)

            # go to the account page
    elif buttonval == 'Select a Book':
        book_name = st.text_input("Enter the book name:")
        question = st.text_input("Enter your Question")
        data1 = {'book_name': book_name}
        data2 = {'book_name': book_name, 'question':question}
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Get Summary"):
                summarizing(data1)
        with col2:
         if st.button("Get Answer"):
            questionAnswering(data2)

