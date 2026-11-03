import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def llm_response(prompt: str):
    """Sends a prompt to the Gemini API and streams the response."""
    print("Sending request to Gemini API...")
    
    # Pass the actual string prompt, not a function object
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
    )

    return interaction.output_text