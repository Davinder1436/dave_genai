from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)


    return response.text

st.set_page_config(page_title= "image demo")

st.header("Image demo Gemini")

input = st.text_input("Input",key="input")
upload_file = st.file_uploader("Upload an image",type=["png","jpg","jpeg"],key="image")
image =""
submit = st.button("Submit Prompt",key="submit")

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)


if submit and image:
    output = get_response(input,image)
    st.subheader("--- Response ---")
    st.write(output)