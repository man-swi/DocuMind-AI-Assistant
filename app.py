import os
import time
import streamlit as st
from utils import (
    extract_text_from_file,
    analyze_text_with_ai,
    chat_with_document,
    preprocess_text,
    setup_vector_db,
    store_document,
    generate_embedding
)
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

# API Key setup for Mistral AI
API_KEY = os.getenv("MISTRAL_API_KEY")

# Streamlit page
st.set_page_config(
    page_title="DocuMind AI Assistant",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #1E88E5;
            text-align: center;
            margin-bottom: 1rem;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #424242;
            text-align: center;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title and Description
st.markdown("<h1 class='main-header'>📚 DocuMind AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Your Intelligent Document Analysis Companion</p>", unsafe_allow_html=True)

# Feature Overview
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🔍 Smart Analysis")
    st.write("Extract key insights and summaries from your documents instantly")

with col2:
    st.markdown("### 💬 Interactive Chat")
    st.write("Have natural conversations about your document content")

with col3:
    st.markdown("### 📄 Multi-Format Support")
    st.write("Works with PDF, Word, and Image files")

# Divider
st.markdown("---")

# Initializing session state for storing extracted text and vector DB
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = None

if 'vector_db' not in st.session_state:
    index, embeddings = setup_vector_db([])  # Initializing vector database
    st.session_state.vector_db = index  # FAISS index
    st.session_state.embeddings = embeddings

# File Uploading Section
st.markdown("### 📎 Upload Your Document")
st.write("Start by uploading your document - we support PDF, Word, and Image files!")
uploaded_file = st.file_uploader("", type=["pdf", "docx", "jpg", "jpeg", "png"])

if uploaded_file:
    st.success(f"✅ Successfully uploaded: {uploaded_file.name}")
    st.session_state.extracted_text = extract_text_from_file(uploaded_file)
    
    if st.session_state.extracted_text == "Unsupported file format!":
        st.error("❌ Unsupported file format! Please upload a PDF, Word, or Image file.")
    else:
        # Preprocessing text before displaying
        processed_text = preprocess_text(st.session_state.extracted_text)

        # Generating embedding and store document
        embedding = generate_embedding(st.session_state.extracted_text)
        store_document(st.session_state.vector_db, st.session_state.extracted_text, embedding)

        # Creating tabs for different functionalities
        tab1, tab2 = st.tabs(["📊 Document Analysis", "💬 Chat with Document"])
        
        with tab1:
            st.markdown("### 📄 Extracted Content")
            st.text_area("", processed_text, height=200)

            if st.button("🔍 Analyze with AI", use_container_width=True):
                if not API_KEY:
                    st.error("🔑 API key not found! Please set the `MISTRAL_API_KEY` environment variable.")
                else:
                    with st.spinner("🤖 AI is analyzing your document..."):
                        start_time = time.time()
                        analysis_result = analyze_text_with_ai(processed_text)
                        response_time = time.time() - start_time
                        if isinstance(analysis_result, dict) and "error" in analysis_result:
                            st.error(f"❌ Error: {analysis_result['error']}")
                        else:
                            st.markdown("### 🎯 Analysis Results")
                            st.write(analysis_result)
                            st.info(f"⚡ Analysis completed in {response_time:.2f} seconds")
        
        with tab2:
            st.markdown("### 💭 Chat with your Document")
            st.info("Ask anything about your document! I'll help you find the information you need.")
            
            # Initializing chat history
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Displaying chat history
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            # Chat input
            if question := st.chat_input("💭 Ask a question about your document..."):
                with st.chat_message("user"):
                    st.markdown(question)
                st.session_state.messages.append({"role": "user", "content": question})

                with st.chat_message("assistant"):
                    with st.spinner("🤔 Thinking..."):
                        start_time = time.time()
                        response = chat_with_document(question, st.session_state.vector_db)
                        response_time = time.time() - start_time
                        if isinstance(response, dict) and "error" in response:
                            st.error(f"❌ Error: {response['error']}")
                        else:
                            st.markdown(response)
                            st.session_state.messages.append({"role": "assistant", "content": response})
                            st.info(f"⚡ Response generated in {response_time:.2f} seconds")

else:
    st.info("👋 Welcome to DocuMind AI Assistant!")
    
    st.markdown("""
    #### 🚀 Getting Started:
    1. Upload your document using the file uploader above.
    2. Choose from two powerful features:
        * 📊 **Document Analysis**: Get comprehensive insights and summaries.
        * 💬 **Interactive Chat**: Ask questions and get instant answers.
    
    #### 📁 Supported Formats:
    * PDF Documents (*.pdf)
    * Word Documents (*.docx)
    * Images (*.jpg, *.jpeg, *.png)
    
    #### ✨ Features:
    * Smart text extraction.
    * AI-powered analysis.
    * Natural conversation interface.
    * Real-time processing.
    """)

st.markdown("---")
st.markdown("### 🌟 Made with AI + Human Intelligence")
st.write("For the best experience, make sure your documents are clear and well-formatted!")
