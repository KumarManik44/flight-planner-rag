import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise RuntimeError("PINECONE_API_KEY not found in .env")

pc = Pinecone(api_key=PINECONE_API_KEY)

INDEX_NAME = "flight-routes-v1"

existing_indexes = [idx["name"] for idx in pc.list_indexes()]

if INDEX_NAME in existing_indexes:
    print(f"Index '{INDEX_NAME}' already exists.")
else:
    print(f"Creating index '{INDEX_NAME}'...")

    pc.create_index(
        name=INDEX_NAME,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    print("Index created successfully.")
