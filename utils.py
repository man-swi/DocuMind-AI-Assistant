import os
from dotenv import load_dotenv
import requests
from PyPDF2 import PdfReader
from docx import Document
from pytesseract import image_to_string
from PIL import Image

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()
    text = ""

    if file_type == "pdf":
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    elif file_type == "docx":
        doc = Document(uploaded_file)
        for paragraph in doc.paragraphs:
            text += paragraph.text

    elif file_type in ["jpg", "jpeg", "png"]:  
        img = Image.open(uploaded_file)
        text = image_to_string(img)  

    else:
        text = "Unsupported file format!"

    return text

def analyze_text_with_ai(text):
    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI document analyzer. Analyze the following text and provide key insights, main topics, and a structured summary."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']
            return analysis
        else:
            return {"error": f"API call failed with status code {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def chat_with_document(question, context):
    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions about documents. Use the provided document context to answer questions accurately. If the answer cannot be found in the document, say so clearly."
            },
            {
                "role": "user",
                "content": f"Document context: {context}\n\nQuestion: {question}"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            return answer
        else:
            return {"error": f"API call failed with status code {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def preprocess_text(text):
    """Preprocess text by removing unnecessary whitespace and special characters."""
    import re
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
    text = re.sub(r'[^a-zA-Z0-9\s.,?!]', '', text)  # Remove special characters
    return text