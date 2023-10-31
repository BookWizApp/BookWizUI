import streamlit as st

from streamlit_option_menu import option_menu


import home, account, about
st.set_page_config(
    page_title="BookWiz",
)
if 'username' not in st.session_state:
    st.session_state.username = ''  # Set the initial value to an empty string or your desired default value




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        if st.session_state.get('switch_button', False):
            st.session_state['menu_option'] = (st.session_state.get('menu_option',1)) 
            manual_select = st.session_state['menu_option']
        else:
            manual_select = None
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='BookWiz ',
                options=['Home','Account','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1, manual_select=manual_select, key='menu_1',
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
            
        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app() 
        if app == 'about':
            about.app() 
             
             
          
             
multi_app = MultiApp()
multi_app.run()          
         
