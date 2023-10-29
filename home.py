import streamlit as st
import random


def app():
    from streamlit.components.v1 import html
    from streamlit_extras.switch_page_button import switch_page
    
    ph = ''
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
        def f():
            try:
                st.session_state["book_selected"] = True
                def summary():
                    st.text("Summary of the book is :")
                    ph = "Summary"
                    post=st.text_area(label=' :orange[+ Book name]',placeholder=ph,height=None, max_chars=500)
                def QA():
                    st.text("Let's start Q/A session") 
                    ph = "Ask your Question"
                    post=st.text_area(label=' :orange[+ Q/A]',placeholder=ph,height=None, max_chars=500)  
                st.button('Generate Summary of the book',on_click=summary,use_container_width=10)
                st.button('Q/A session regarding the book',on_click=QA,use_container_width=10)  

            except:
                return None 
                
        
        if "book_selected"  not in st.session_state :
            st.session_state["book_selected"] = False
        if  not st.session_state["book_selected"]:
            st.button('Select a Book',use_container_width=20,on_click=f,key = random.randint(0,1000))
        else:
            f()  