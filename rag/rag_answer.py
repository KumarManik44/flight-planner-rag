from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(user_query: str, retrieved_route: dict | None):
    """
    Generate a grounded answer using retrieved route metadata.
    If no route is found, respond safely.
    """

    if retrieved_route is None:
        return (
            "Sorry, I don't have reliable flight data for that route yet. "
            "Please try another city pair."
        )

    metadata = retrieved_route["metadata"]

    prompt = f"""
You are a flight information assistant.

Answer the user's question using ONLY the data below.
Do NOT invent prices, airlines, or durations.
If something is missing, say so clearly.

Route details:
- Origin: {metadata['origin_city']} ({metadata['origin']})
- Destination: {metadata['destination_city']} ({metadata['destination']})
- Airlines: {", ".join(metadata['airlines'])}
- Average price range: INR {metadata['avg_price_min']} to INR {metadata['avg_price_max']}
- Typical duration: {metadata['duration_min_minutes']} to {metadata['duration_max_minutes']} minutes
- Time patterns: {", ".join(metadata['time_bias'])}
- Last updated: {metadata['last_updated']}

User question:
{user_query}

Answer clearly and concisely.
"""

    response = genai_client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[prompt]
    )

    return response.text.strip()
