import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
INDEX_NAME = "conspiracy-theories-vector-index"

def vector_search(query_text: str, top_k: int = 3):
    """Searches the Pinecone index for chunks semantically matching the query text."""
    index = pc.Index(INDEX_NAME)

    response = index.search_records(
        namespace="conspiracy_theories_namespace",
        query={
            "top_k": top_k,  # Fixed: changed from 'topk' to 'top_k'
            "inputs": {"text": query_text}  # Pinecone Integrated Inference expects inputs matching your field map
        }
    )

    return response