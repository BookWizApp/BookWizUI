import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import requests
flask_app_url = 'http://36c6-34-125-201-121.ngrok-free.app'
def summarizing(data):
    response = requests.post(f'{flask_app_url}/get_summary', json=data)
    print(response)
    summary = response.json().get('summary')
    st.write(f"Summary: {summary}")
def questionAnswering(data):  
    response = requests.post(f'{flask_app_url}/get_answer', json=data)
    print(response)
    answer = response.json().get('answer')
    st.write(f"Answer: {answer}")
def app():
    st.title("Book Summary Generator")
    st.sidebar.title("Options")
    book_name = st.text_input("Enter the book name:")
    question = st.text_input("Enter your Question")
    data = {'book_name': book_name, 'question':question}
    if st.button("Get Summary"):
        summarizing(data)
    if st.button("Get Answer"):
        questionAnswering(data)