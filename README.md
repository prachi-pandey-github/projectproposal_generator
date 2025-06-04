# Client Proposal Generator

This project is a Client Proposal Generator that takes client requirements as input and uses AI to generate a project proposal or pitch deck outline. It utilizes LangChain, Gemini API, and Streamlit to provide an interactive user experience.

## Project Structure

```
client-proposal-generator
├── src
│   ├── app.py                # Main entry point of the application
│   ├── ai
│   │   ├── langchain_utils.py # Utility functions for LangChain integration
│   │   ├── gemini_api.py      # Interaction with the Gemini API
│   │   └── proposal_generator.py # Class for generating proposals
│   ├── ui
│   │   └── streamlit_ui.py    # Streamlit UI components
│   └── utils
│       └── helpers.py         # Helper functions for the application
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd client-proposal-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Open the application in your web browser.
- Input the client requirements in the provided fields.
- Click on the button to generate the project proposal or pitch deck outline.
- Review the generated content and make any necessary adjustments.

## Overview of Functionality

The Client Proposal Generator allows users to input specific client requirements and leverages AI to create tailored project proposals. The application is designed to streamline the proposal generation process, making it easier for users to present their ideas effectively.