# filepath: c:\Users\dell\Desktop\mood\client-proposal-generator\client-proposal-generator\src\app.py

import streamlit as st
from ui.streamlit_ui import create_ui
from ai.proposal_generator import ProposalGenerator

def main():
    st.title("Client Proposal Generator")
    st.write("Welcome to the Client Proposal Generator. Please provide your requirements below.")
    
    # Create the Streamlit UI
    create_ui()

if __name__ == "__main__":
    main()