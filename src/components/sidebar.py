import streamlit as st

def render_sidebar():
    # Custom CSS for sidebar styling
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background-color: #F7F4EC;
            border-right: 1px solid rgba(40, 49, 51, 0.1);
        }
        [data-testid="stSidebar"] .sidebar-content {
            padding: 1rem;
        }
        [data-testid="stSidebarNav"] {
            background-color: #F7F4EC;
        }
        /* Improved text contrast for headers and text */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {
            color: #283133;
            font-weight: 600;
        }
        [data-testid="stSidebar"] .stMarkdown {
            color: #283133;
        }
        /* Selectbox styling */
        .stSelectbox [data-testid="stMarkdownContainer"] {
            color: #283133;
            font-weight: 500;
        }
        .stSelectbox > div > div {
            background-color: white;
            border: 1px solid #D5DA5E;
            border-radius: 8px;
            color: #283133;
        }
        .stSelectbox > div > div:hover {
            border: 1px solid #C1C745;
        }
        /* User info container styling */
        .user-info-container {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid rgba(40, 49, 51, 0.1);
            color: #283133;
        }
        /* Status indicator styling */
        .status-indicator {
            background-color: #D5DA5E;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            color: #283133;
            font-weight: 500;
            font-size: 0.9em;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # Logo section
        st.image("src/assets/One_80_LightLogo.jpg", width=500)
        # st.markdown("---")
        
        # User info section with styled containers
        st.markdown('<div class="user-info-container">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #283133; margin-bottom: 1rem;">User Info</h3>', unsafe_allow_html=True)
        
        # Get user info from session state
        if 'user' in st.session_state:
            user = st.session_state['user']
            st.markdown(f'''
                <p style="color: #283133;">
                    <strong>👤 Username:</strong> {user.get('username', 'N/A')}<br>
                    <strong>🏢 Company:</strong> {user.get('company', 'N/A')}<br>
                    <strong>🔑 Role:</strong> {user.get('role', 'N/A')}
                </p>
            ''', unsafe_allow_html=True)
        else:
            st.warning("User not logged in", icon="⚠️")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Navigation section
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<h3 style="color: #283133;">Menu</h3>', unsafe_allow_html=True)
        selected_service = st.selectbox(
            "Select Service",
            ["RAG Chat", "Document Processing", "Settings"],
            key="service_selection"
        )
        
        # Status section with styled info box
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<h3 style="color: #283133;">System Status</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div class="status-indicator">
            ✅ EarthlyAI Connection: Active
            </div>
        """, unsafe_allow_html=True)
        
        # Add separator before the button
        st.markdown("---")
        
        # # Add the Social Media Automation button for the Form
        # if st.button("📱 Social Media Automation", 
        #             use_container_width=True,
        #             type="primary",
        #             help="Click to open the automation form"):
        #     # Open n8n form in new tab
        #     js = f"""
        #     <script>
        #         window.open(
        #             "https://rubencasillas.app.n8n.cloud/form/3e762442-715e-47e1-a65e-ae92085857ae",
        #             "_blank"
        #         );
        #     </script>
        #     """
        #     st.components.v1.html(js)

        
        # Logout section
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Logout", 
                    type="primary", 
                    use_container_width=True,
                    help="Click to log out from your account"):
            st.session_state.clear()
            st.rerun()

# Call the function to create the sidebar
if __name__ == "__main__":
    render_sidebar()