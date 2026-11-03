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
    stream = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )

    print("Stream connected, awaiting chunks...")
    for event in stream:
        if hasattr(event, "delta") and event.delta:
            print(event.delta, end="", flush=True)
        else:
            print(event)

if __name__ == "__main__":
    # Test locally with a hardcoded string prompt
    llm_response("Explain quantum computing in one sentence.")