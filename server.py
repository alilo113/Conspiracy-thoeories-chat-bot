from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class UserPrompt(BaseModel):
    prompt: str

@app.post('/prompt')
def process_prompt(request: Request):
    try:
        data = request.json()
        prompt = data.get('prompt', '')
        if not prompt:
            raise HTTPException(status_code=400, detail='Prompt is required')

        # Process the prompt (e.g., send to a backend service)
        response = {'status': 'success', 'message': 'Prompt processed successfully'}

        return response
    except Exception as e:
        return {'status': 'error', 'message': str(e)}