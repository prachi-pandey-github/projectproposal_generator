import streamlit as st
import google.generativeai as genai

class GeminiAPI:
    def __init__(self):
        self.api_key = st.secrets["gemini"]["api_key"]
        self.model = st.secrets["gemini"]["model"]  
        genai.configure(api_key=self.api_key)
        self.model_obj = genai.GenerativeModel(self.model)

    def generate_proposal(self, client_requirements):
        prompt = f"Generate a client proposal for the following requirements: {client_requirements}"
        response = self.model_obj.generate_content(prompt)
        return response.text

    def generate_pitch_deck(self, client_requirements):
        prompt = f"Generate a pitch deck for the following requirements: {client_requirements}"
        response = self.model_obj.generate_content(prompt)
        return response.text
