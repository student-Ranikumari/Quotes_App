import streamlit as st
import os
from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.2,
    groq_api_key="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"  # Replace with actual API key
)

# Function to generate a quote
def generate_quote(category):
    prompt = f"Generate a {category} quote."
    return llm.predict(prompt)

# Function to save quote as file
def save_quote(quote):
    with open("generated_quote.txt", "w") as file:
        file.write(quote)
    st.success("Quote saved as 'generated_quote.txt'")

# Streamlit UI
st.title("AI-Powered Quote Generator")

# Quote Categories
category = st.selectbox("Select Quote Category", ["Motivational", "Inspirational", "Random"])

# Session state for quote
if "quote" not in st.session_state:
    st.session_state["quote"] = ""

if st.button("Generate Quote"):
    st.session_state["quote"] = generate_quote(category)

st.text_area("Generated Quote", st.session_state["quote"], height=100)

# Copy Button
st.button("Copy Quote", on_click=lambda: st.session_state.update({"copied": st.session_state["quote"]}))

# Save Button
if st.button("Save Quote as File"):
    save_quote(st.session_state["quote"])

# Clear Button
if st.button("Clear Quote"):
    st.session_state["quote"] = ""

st.write("Powered by Groq LLM & LangChain 🚀")
