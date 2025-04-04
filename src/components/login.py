import streamlit as st
from pathlib import Path
import logging
from auth.authentication import login, register
import base64

logger = logging.getLogger(__name__)

def get_base64_encoded_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logger.error(f"Failed to load image: {str(e)}")
        return None

def login_page():
    try:
        # Page configuration for login - centered and narrow
        st.set_page_config(
            page_title="One80 Automation Dashboard Login",
            # page_icon="🍄",
            layout="centered",
            initial_sidebar_state="collapsed"
        )
        
        # Custom CSS for login page
        st.markdown("""
            <style>
            .block-container {
                max-width: 800px !important;
                padding: 2rem !important;
            }
            .login-container {
                background-color: white;
                padding: 2rem;
                border-radius: 15px;
                border: 1px solid rgba(40, 49, 51, 0.1);
                box-shadow: 0 4px 6px rgba(40, 49, 51, 0.05);
                margin: 2rem auto;
                max-width: 400px;
            }
            .stApp {
                background-color: #F7F4EC; /* soft mushroom beige */
                color: #2D2A26; /* high-contrast dark mushroom brown for text */
            }
            .block-container {
                max-width: 800px !important;
                padding: 2rem !important;
            }
            .login-container {
                background-color: white;
                padding: 2rem;
                border-radius: 15px;
                border: 1px solid rgba(40, 49, 51, 0.1);
                box-shadow: 0 4px 6px rgba(40, 49, 51, 0.05);
                margin: 2rem auto;
                max-width: 400px;
            }
            .main > div {
                padding-top: 1rem;
            }


            /* Footer Styling */
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                text-align: center;
                padding: 1rem;
                background-color: rgba(247, 244, 236, 0.95);
                color: #3C403D;
                font-size: 0.8rem;
                backdrop-filter: blur(10px);
            }

            /* Text Input Styling */
            .stTextInput > div > div {
                background-color: #283133;
                border-radius: 10px;
                border: 1px solid #D5DA5E;
            }
            
            /* Input text color */
            .stTextInput input {
                color: #D5DA5E !important;  /* Vivid Tech color */
                font-weight: 500 !important;
            }
            
            /* Placeholder text color */
            .stTextInput input::placeholder {
                color: rgba(213, 218, 94, 0.6) !important;  /* Vivid Tech with opacity */
            }

            /* Button Styling */
            .stButton > button {
                background-color: #D5DA5E !important; /* primary branding lime-green */
                color: #1F1F1F !important;
                border-radius: 10px !important;
                border: none !important;
                padding: 0.75rem 2rem !important;
                font-weight: 600 !important;
                width: 100% !important;
                transition: all 0.3s ease !important;
            }

            .stButton > button:hover {
                background-color: #C1C745 !important;
                box-shadow: 0 4px 10px rgba(40, 49, 51, 0.15) !important;
                transform: translateY(-5px);
                color: #000000 !important;
            }

            /* Tabs Styling */
            .stTabs {
                background-color: #D5DA5E;
                border-radius: 15px;
                padding: 1rem;
            }

            .stTab {
                background-color: #D5DA5E;
            }

            .stTab > div {
                background-color: transparent;
                color: #2D2A26 !important;
                border-radius: 8px !important;
                padding: 0.5rem 1.5rem !important;
            }

            .stTab [aria-selected="true"] {
                background-color: #D5DA5E !important;
                font-weight: 600;
                color: #1F1F1F !important;
            }
            </style>
        """, unsafe_allow_html=True)

        # # Logo container
        # col1, col2, col3 = st.columns([1, 2, 1])
        # with col2:
        #     st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        #     logo_path = "src/assets/One_80_lightLogo.jpg"
        #     st.image(logo_path, width=500)
        #     st.markdown('</div>', unsafe_allow_html=True)

        # # Login container
        # st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Login/Register tabs
        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            st.subheader("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                if st.button("Login", use_container_width=True):
                    try:
                        if login(username, password):
                            st.session_state['authentication_status'] = True
                            st.rerun()  # Use rerun instead of experimental_rerun
                        else:
                            st.error("Invalid username or password")
                    except Exception as e:
                        logger.error(f"Login error: {str(e)}")
                        st.error("An error occurred during login. Please try again.")

        with tab2:
            st.subheader("Register")
            new_username = st.text_input("Username", key="register_username")
            new_password = st.text_input("Password", type="password", key="register_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
            company = st.text_input("Company Name")
            
            # Password requirements hint
            st.markdown("""
                <div style='font-size: 0.8em; color: #666;'>
                Password requirements:
                - At least 8 characters
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                if st.button("Register", use_container_width=True):
                    if new_password != confirm_password:
                        st.error("Passwords do not match")
                    else:
                        success, message = register(new_username, new_password, company)
                        if success:
                            st.success(message)
                            st.rerun()  # Use rerun instead of experimental_rerun
                        else:
                            st.error(message)
                            st.rerun()  # Use rerun instead of experimental_rerun

        st.markdown('</div>', unsafe_allow_html=True)

        # Footer
        st.markdown(
            '<div class="footer">Designed by EarthlyAI </div>',
            # page_icon="c_icon.ico",
            unsafe_allow_html=True
        )
    except Exception as e:
        logger.error(f"Page error: {str(e)}")
        st.error("An error occurred while loading the page. Please refresh.")
