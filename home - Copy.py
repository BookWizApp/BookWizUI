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
    st.title("Book Summary Generator")
    st.sidebar.title("Options")
    book_name = st.text_input("Enter the book name:")
    question = st.text_input("Enter your Question")
    data1 = {'book_name': book_name}
    data2 = {'book_name': book_name, 'question':question}
    if st.button("Get Summary"):
        summarizing(data1)
    if st.button("Get Answer"):
        questionAnswering(data2)