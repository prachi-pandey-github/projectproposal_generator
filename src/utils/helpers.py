def validate_client_requirements(requirements):
    if not isinstance(requirements, dict):
        raise ValueError("Client requirements must be provided as a dictionary.")
    
    required_keys = ['project_name', 'description', 'budget', 'timeline']
    for key in required_keys:
        if key not in requirements:
            raise ValueError(f"Missing required key: {key}")
    
    return True

def format_requirements_for_ai(requirements):
    formatted = f"Project Name: {requirements['project_name']}\n"
    formatted += f"Description: {requirements['description']}\n"
    formatted += f"Budget: {requirements['budget']}\n"
    formatted += f"Timeline: {requirements['timeline']}\n"
    return formatted

def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{error_message}\n")