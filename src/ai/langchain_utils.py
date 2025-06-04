def process_client_requirements(requirements):
    # Process the client requirements to a suitable format for AI processing
    processed_requirements = {
        "summary": requirements.get("summary"),
        "details": requirements.get("details"),
        "budget": requirements.get("budget"),
        "timeline": requirements.get("timeline"),
    }
    return processed_requirements
def process_requirements(client_requirements):
    # Example: just return the input for now, or add your processing logic
    return client_requirements

def format_for_langchain(processed_requirements):
    # Format the processed requirements for LangChain input
    formatted_input = f"""
    Client Summary: {processed_requirements['summary']}
    Project Details: {processed_requirements['details']}
    Budget: {processed_requirements['budget']}
    Timeline: {processed_requirements['timeline']}
    """
    return formatted_input.strip()
