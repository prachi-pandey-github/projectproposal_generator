import streamlit as st
from ai.proposal_generator import ProposalGenerator
from ai import langchain_utils, gemini_api

def create_ui():
    st.header("Enter Client Requirements")
    client_name = st.text_input("Client Name")
    project_description = st.text_area("Project Description")
    budget = st.number_input("Budget", min_value=0.0, format="%.2f")
    deadline = st.date_input("Deadline")

    if st.button("Generate Proposal"):
        if client_name and project_description:
            proposal_generator = ProposalGenerator(langchain_utils, gemini_api.GeminiAPI())
            proposal = proposal_generator.generate_proposal(client_name, project_description, budget, deadline)
            st.subheader("Generated Proposal")
            st.write(proposal)
        else:
            st.error("Please fill in all required fields.")