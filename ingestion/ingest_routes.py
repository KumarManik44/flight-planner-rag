import json
import os
from pathlib import Path
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
# Load routes data
# ----------------------------
PROJECT_ROOT = Path.cwd()
DATA_PATH = PROJECT_ROOT / "data" / "routes_v1.json"

print("PROJECT_ROOT =", PROJECT_ROOT)
print("DATA_PATH =", DATA_PATH)
print("Exists?", DATA_PATH.exists())


with open(DATA_PATH, "r") as f:
    routes = json.load(f)


print(f"Loaded {len(routes)} routes.")

# ----------------------------
# Clear existing vectors
# ----------------------------
print("Deleting existing vectors...")
index.delete(delete_all=True)

# ----------------------------
# Batch embed + upsert
# ----------------------------
vectors = []

for route in routes:
    document_text = (
        f"Flights from {route['origin_city']} ({route['origin']}) "
        f"to {route['destination_city']} ({route['destination']}). "
        f"Typical airlines include {', '.join(route['airlines'])}. "
        f"Average prices range from INR {route['avg_price_min']} "
        f"to INR {route['avg_price_max']}. "
        f"Typical duration ranges from {route['duration_min_minutes']} "
        f"to {route['duration_max_minutes']} minutes. "
        f"Time patterns: {', '.join(route['time_bias'])}."
    )

    embedding_response = genai_client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[document_text]
    )

    vector = embedding_response.embeddings[0].values

    vectors.append({
        "id": route["id"],
        "values": vector,
        "metadata": route
    })

# ----------------------------
# Upsert into Pinecone
# ----------------------------
print("Upserting vectors into Pinecone...")
index.upsert(vectors)

print("✅ Batch ingestion complete.")
