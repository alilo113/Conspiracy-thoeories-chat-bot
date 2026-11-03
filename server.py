from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag.llm import llm_response

app = FastAPI()

# Define the expected JSON body structure using Pydantic
class PromptSchema(BaseModel):
    prompt: str

@app.post("/user-prompt")
def receive_prompt(payload: PromptSchema):
    try:
        llm_response(payload.prompt)
        return {"message": "Prompt processed", "prompt": payload.prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
