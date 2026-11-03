import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_rag_response(user_query: str, retrieved_titles: list[str]) -> str:
    """Builds a grounded prompt using retrieved vector search results and queries Gemini."""
    
    # Format the retrieved titles into a clean context block
    context = "\n".join([f"- {title}" for title in retrieved_titles])
    
    # Structure the prompt so the LLM relies on your retrieved data
    structured_prompt = f"""
You are an eccentric conspiracy theorist AI assistant.
Your goal is to answer EVERY user question by steering the topic directly to the conspiracy theory video titles provided in the Context.

No matter what the user asks (even if it's unrelated or personal like "Describe yourself!"), pivot the conversation and explain your answer through the lens of these specific conspiracy topics:

Context / Evidence:
{context}

User Question: {user_query}

Answer in character, weaving the provided context titles directly into your response:
"""

    print("Sending RAG request to Gemini API...")
    response = client.models.generate_content(
        model="gemini-3.5-flash",  # Updated to the active current model endpoint
        contents=structured_prompt,
    )

    return response.text