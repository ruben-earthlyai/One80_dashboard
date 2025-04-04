import streamlit as st
import streamlit.components.v1 as components

def render_form():
    st.header("Service Request Form")

    # Custom CSS for the container
    st.markdown("""
        <style>
        .form-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Container for the n8n form
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        # Replace this URL with your actual n8n webhook form URL
        n8n_form_url = "https://rubencasillas.app.n8n.cloud/form/3e762442-715e-47e1-a65e-ae92085857ae"
        
        # Embed the n8n form using an iframe
        components.iframe(
            n8n_form_url,
            height=600,
            scrolling=True
        )
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Optional: Add a status indicator
    with st.expander("Form Submission Status"):
        st.info("Forms are processed through n8n cloud workflow")
        st.markdown("""
        - ✅ Secure submission
        - 📨 Instant notification
        - 🔄 Automated workflow
        """)