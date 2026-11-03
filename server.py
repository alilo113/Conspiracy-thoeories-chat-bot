from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag.retrieval import vector_search
from rag.llm import generate_rag_response

app = FastAPI()

class PromptSchema(BaseModel):
    prompt: str

@app.post("/user-prompt")
def handle_user_prompt(payload: PromptSchema):
    try:
        # Explicitly pass top_k=3 here to prevent any NoneType passing
        search_results = vector_search(query_text=payload.prompt)

        retrieved_titles = []
        for match in search_results.get("result", {}).get("hits", []):
            title = match.get("fields", {}).get("chunked_titles")
            if title:
                retrieved_titles.append(title)

        ai_answer = generate_rag_response(
            user_query=payload.prompt, 
            retrieved_titles=retrieved_titles
        )

        return {
            "user_prompt": payload.prompt,
            "retrieved_sources": retrieved_titles,
            "response": ai_answer
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))