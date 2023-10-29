import streamlit as st
import pyrebase
from datetime import datetime


firebaseConfig = {
  'apiKey': "AIzaSyBrUNqVFHCb8SWW0m50LPaEYCFd7C9p5fw",
  'authDomain': "dse-final-project-a7b1a.firebaseapp.com",
  'projectId': "dse-final-project-a7b1a",
  'databaseURL':"https://dse-final-project-a7b1a-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'storageBucket': "dse-final-project-a7b1a.appspot.com",
  'messagingSenderId': "14810971237",
  'appId': "1:14810971237:web:881fa306b9858f04415a8c",
  'measurementId': "G-SWM8JLHSMJ"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
def app():
    st.title('Welcome to :violet[BookWiz] :sunglasses:')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''



    def f(): 
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.username = db.child(user['localId']).child("Handle").get().val()
            st.session_state.useremail = user['email']
            
            st.session_state.signedout = True
            st.session_state.signout = True  

        except: 
            st.warning('Incorrect Username or Password')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        st.session_state["book_selected"] = False

        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user_with_email_and_password(email, password)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
                db.child(user['localId']).child("Handle").set(username)
                db.child(user['localId']).child("ID").set(user['localId'])
        else:        
            st.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                st.text('Hi '+st.session_state.username)
                st.text('You are logged using the email address '+st.session_state.useremail)
                st.button('Sign out', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Posts')
