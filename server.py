from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the expected JSON body structure using Pydantic
class PromptSchema(BaseModel):
    prompt: str

@app.post("/user-prompt")
def receive_prompt(payload: PromptSchema):
    # FastAPI automatically ensures 'prompt' exists and is a string
    prompt = payload.prompt
    
    # Your logic here
    return {"message": "Prompt received", "received_prompt": prompt}