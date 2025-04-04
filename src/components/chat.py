import streamlit as st
import requests
import uuid
from typing import Optional

# Constants
N8N_WEBHOOK_URL = "https://rubencasillas.app.n8n.cloud/webhook/8dc8b133-8516-475d-99e0-5d557f5b1858"
BEARER_TOKEN = "tech4Life@all"

def get_session_id() -> str:
    """Get or create a session ID for the current chat session."""
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id

def send_message_to_llm(message: str, session_id: str) -> Optional[str]:
    """Send message to LLM through n8n webhook and return response."""
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {  
        "sessionId": session_id,
        "chatInput": message
    }
    
    try:
        response = requests.post(N8N_WEBHOOK_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["output"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with LLM: {str(e)}")
        return None

def render_chat():
    st.subheader("One80 Assistant")
    
    # Initialize chat history and session
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    session_id = get_session_id()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Ready for some Trading?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get LLM response through n8n webhook
        with st.spinner("Thinking the best trading strategy..."):
            llm_response = send_message_to_llm(prompt, session_id)
            
        # Display assistant response
        with st.chat_message("assistant"):
            if llm_response:
                st.markdown(llm_response, unsafe_allow_html=True)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": llm_response})
    
    # Clear chat button with session reset
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("Clear Chat", key="clear_chat"):
            st.session_state.messages = []
            st.session_state.session_id = str(uuid.uuid4())  # Generate new session
            st.rerun()