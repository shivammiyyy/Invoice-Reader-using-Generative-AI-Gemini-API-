from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("generative_api_key"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        byte_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": byte_data
            }
        ]
        return image_parts
    
    else:
        raise FileExistsError("No file uploaded")
    

st.set_page_config(page_title="Invoice Extractor")

st.header("Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("choose an image... ",type=["jpg","jpef","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt="""
you are an expert in understanding invoices. we will upload an image as invoice 
and you will have to answer any questions based on the invoice uploaded
"""
if submit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)