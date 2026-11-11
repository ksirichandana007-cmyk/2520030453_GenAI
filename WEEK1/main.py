
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found! Check your .env file.")

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display the response
print("\nLLM Response:")
print(response.text)