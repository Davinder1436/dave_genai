from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)

    return response.text

st.set_page_config(page_title= "Q&A demo")

st.header("Gemini LLM demo")

input = st.text_input("Input",key="input")
submit = st.button("Submit Prompt",key="submit")

if submit:
    output = get_response(input)
    st.subheader("--- Response ---")
    st.write(output)



