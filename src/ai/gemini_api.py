import streamlit as st
import requests

class GeminiAPI:
    def __init__(self):
        self.api_key = st.secrets["gemini"]["api_key"]
        self.model = st.secrets["gemini"]["model"]
        self.base_url = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

    def generate_proposal(self, client_requirements):
        endpoint = f"{self.base_url}/generate_proposal"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "requirements": client_requirements,
            "model": self.model
        }
        response = requests.post(endpoint, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def generate_pitch_deck(self, client_requirements):
        endpoint = f"{self.base_url}/generate_pitch_deck"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "requirements": client_requirements,
            "model": self.model
        }
        response = requests.post(endpoint, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
