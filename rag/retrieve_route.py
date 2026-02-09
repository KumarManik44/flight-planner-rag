import os
from dotenv import load_dotenv
from google import genai
from pinecone import Pinecone

# ----------------------------
# Setup
# ----------------------------
load_dotenv()

genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("flight-routes-v1")

# ----------------------------
# Config
# ----------------------------
TOP_K = 3
SIMILARITY_THRESHOLD = 0.75  # critical to avoid hallucination

# ----------------------------
# Retrieve route
# ----------------------------
def retrieve_route(user_query: str):
    """
    Returns the best matching route metadata
    or None if similarity is too low
    """

    embedding_response = genai_client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[user_query]
    )

    query_vector = embedding_response.embeddings[0].values

    results = index.query(
        vector=query_vector,
        top_k=TOP_K,
        include_metadata=True
    )

    if not results["matches"]:
        return None

    best_match = results["matches"][0]

    if best_match["score"] < SIMILARITY_THRESHOLD:
        return None

    return {
        "score": best_match["score"],
        "metadata": best_match["metadata"]
    }
