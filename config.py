import os
from dotenv import find_dotenv, load_dotenv

# Automatically find the .env file
env_path = find_dotenv()

if env_path:  # Ensure a valid .env file is found
    load_dotenv(env_path, override=True)
else:
    print("Warning: .env file not found!")
    
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HYPERLIQUID_API_KEY = os.getenv("HYPERLIQUID_API_KEY")