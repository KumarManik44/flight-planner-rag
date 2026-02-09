import streamlit as st
from rag.retrieve_route import retrieve_route
from rag.rag_answer import generate_answer

# ----------------------------
# Config
# ----------------------------
st.set_page_config(
    page_title="Flight Planner Chatbot",
    page_icon="✈️",
    layout="centered"
)

CITIES = {
    "Mumbai": "BOM",
    "Delhi": "DEL",
    "Bangalore": "BLR",
    "Hyderabad": "HYD",
}

# ----------------------------
# UI
# ----------------------------
st.title("✈️ Flight Planner")
st.caption("Typical domestic flight information powered by Gemini + Pinecone")

st.write("Select two cities to view typical flight details.")

col1, col2 = st.columns(2)

with col1:
    origin_city = st.selectbox(
        "From",
        options=list(CITIES.keys())
    )

with col2:
    destination_city = st.selectbox(
        "To",
        options=list(CITIES.keys())
    )

# Prevent same-city queries
if origin_city == destination_city:
    st.warning("Please select two different cities.")
    st.stop()

if st.button("Get flight information"):
    user_query = f"Flights from {origin_city} to {destination_city}"

    with st.spinner("Retrieving flight data..."):
        retrieved = retrieve_route(user_query)

    answer = generate_answer(user_query, retrieved)

    st.subheader("Flight Information")
    st.write(answer)

    if retrieved:
        with st.expander("🔍 Retrieved route data"):
            st.json(retrieved["metadata"])
