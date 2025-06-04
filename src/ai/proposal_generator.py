class ProposalGenerator:
    def __init__(self, langchain_utils, gemini_api):
        self.langchain_utils = langchain_utils
        self.gemini_api = gemini_api

    def generate_proposal(self, client_requirements):
        processed_requirements = self.langchain_utils.process_requirements(client_requirements)
        proposal = self.gemini_api.send_request(processed_requirements)
        return proposal

    def generate_pitch_deck(self, client_requirements):
        processed_requirements = self.langchain_utils.process_requirements(client_requirements)
        pitch_deck = self.gemini_api.send_request(processed_requirements, pitch_deck=True)
        return pitch_deck