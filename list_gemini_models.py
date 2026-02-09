import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

# Initialize client
client = genai.Client(api_key=api_key)

print("\nAvailable Gemini models:\n")

for model in client.models.list():
    print(f"Name: {model.name}")
    print(f"  Supported methods: {model.supported_actions}")
    print("-" * 60)
