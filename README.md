# ✈️ Flight Planner RAG

A production-grade **Retrieval-Augmented Generation (RAG)** application that provides **typical domestic flight information between major Indian cities**, powered by **Gemini embeddings**, **Pinecone vector search**, and a **Streamlit UI**.

This project is designed to demonstrate how to build a **hallucination-resistant, domain-scoped LLM system** using structured data, vector databases, and a clean, user-safe interface.

---

## 🚀 Live Demo

[**Try the App Here**](https://flight-planner-rag.streamlit.app/)

## 🚀 Features

- 🔍 RAG-based retrieval using Pinecone (no hallucinated answers)
- 🧠 Gemini embeddings for semantic search
- 🗂️ Structured route metadata (prices, duration, airlines, time bias)
- 🎛️ Dropdown-based UI to eliminate user input errors
- ⚡ Fast and cost-efficient (no free-form prompts)
- 🔐 Secure API key handling (no secrets in code)
- 🧪 Fully runnable locally and deployable to Streamlit Cloud

---

## 🧱 Architecture Overview

User (Streamlit UI)
↓
City Selection (From → To)
↓
Vector Query (Gemini Embedding)
↓
Pinecone Vector Search
↓
Relevant Route Metadata
↓
Grounded Natural Language Response


This architecture ensures:
- Deterministic retrieval
- No dependency on real-time scraping
- Stable, explainable outputs

---

## 📂 Project Structure

```
flight-planner-rag/
│
├── app.py                   # Streamlit application
├── requirements.txt
├── .env                     # Local only (not committed)
│
├── data/
│ └── routes_v1.json         # Structured route dataset
│
├── ingestion/
│ ├── create_index.py        # Pinecone index creation
│ └── ingest_routes.py       # Batch ingestion into Pinecone
│
├── rag/
│ └── retrieve_route.py      # Vector retrieval logic
│
└── list_gemini_models.py    # Utility script
```


---

## 🏙️ Supported Cities & Routes

Currently supported cities:
- **Mumbai (BOM)**
- **Delhi (DEL)**
- **Bangalore (BLR)**
- **Hyderabad (HYD)**

All **bi-directional routes** between these cities are included.

Examples:
- BLR → HYD
- HYD → BLR
- DEL → BOM
- BOM → DEL

---

## 🔐 API Keys & Secrets

This project uses **environment variables** for all secrets.

### Required API Keys

- **Gemini API Key**
- **Pinecone API Key**

---

### Local Development

Create a `.env` file in the project root (this file should NOT be committed):

```env
GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
```
Ensure .env is included in .gitignore.

## 🧪 Example Usage

- Select From and To cities using dropdowns
- Click Get flight information

View:

- Airlines
- Price range
- Typical duration
- Time-based pricing patterns
- Expand Retrieved route data to inspect metadata

## 🧠 Why This Project Exists

This is not a prompt-based chatbot.

It demonstrates:

- Real-world RAG design patterns
- Vector schema and metadata modeling
- Grounded generation with zero hallucination
- Production-safe UI decisions
- Cost-aware LLM usage

Ideal for:

- AI Engineer portfolios
- RAG learning references
- Interview demonstrations
- Build-in-public projects

## 🔮 Possible Extensions

- Add more cities by extending the dataset
- Add filters (price, duration)
- Add response caching
- Convert to an API backend
- Extend to trains or hotels
- Add analytics or logging

## 📄 License

MIT License

## 👤 Author

# Kumar Manik
AI Engineer · Builder · Content Creator
