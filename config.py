import os
from dotenv import load_dotenv

# Load the local secrets from .env
load_dotenv()

def initialize_agent():
    api_key = os.getenv("DEVELOPER_API_KEY")
    system_id = os.getenv("INTERNAL_SYSTEM_ID")
    
    if not api_key:
        print("Error: No API Key found in local .env file.")
        return
    
    print(f"Agent successfully initialized for System: {system_id}")
    return api_key

if __name__ == "__main__":
    initialize_agent()