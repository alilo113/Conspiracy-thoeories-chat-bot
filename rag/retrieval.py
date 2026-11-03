import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
INDEX_NAME = "conspiracy-theories-vector-index"

def vector_search(query_text: str):
    """Searches the Pinecone index for chunks semantically matching the query text."""
    index = pc.Index(INDEX_NAME)

    # Use index.search with top_k passed as a top-level parameter
    response = index.search(
        namespace="conspiracy_theories_namespace",
        top_k=3,
        inputs={"text": query_text}
    )

    return response