import os
from dotenv import load_dotenv
import requests
from PyPDF2 import PdfReader
from docx import Document
from pytesseract import image_to_string
from PIL import Image
import faiss
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import re

# Loading environment variables from .env file
load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

# Load tokenizer and model once at the start
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()
    text = ""

    if file_type == "pdf":
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

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
    
    # Text analysis
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

def chat_with_document(question, vector_db):
    context = retrieve_context_from_db(question, vector_db) 
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
    text = re.sub(r'\s+', ' ', text)  # Removing extra whitespaces
    text = re.sub(r'[^a-zA-Z0-9\s.,?!]', '', text)  # Removing special characters
    return text

def generate_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)  
    return embeddings.numpy().flatten()

def extract_embeddings(documents):
    embeddings = []
    for doc in documents:
        embeddings.append(generate_embedding(doc))
    return np.array(embeddings)

def setup_vector_db(documents):
    if not documents:
        dim = 768  
        index = faiss.IndexFlatL2(dim)
        return index, None
    
    document_embeddings = extract_embeddings(documents)
    dim = document_embeddings.shape[1] 
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(document_embeddings, dtype=np.float32))
    return index, document_embeddings

def store_document(index, document, embedding):
    """Store a document's embedding in the vector database."""
    if index.d != len(embedding):
        raise ValueError(f"Embedding dimension {len(embedding)} does not match index dimension {index.d}.")
    index.add(np.array([embedding], dtype=np.float32))

def retrieve_context_from_db(question, vector_db):
    return "This is a placeholder for retrieved context based on the question."

def get_document_embedding(text):
    return np.random.rand(512)
