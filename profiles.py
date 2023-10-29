import streamlit as st

  
def app():


    try:
        st.title("Welcome to profile page")       

        
    except:
        if st.session_state.username=='':
            st.text('Please Login first')        