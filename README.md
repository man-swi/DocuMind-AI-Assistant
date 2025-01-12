# DocuMind AI Assistant

📚 **DocuMind AI Assistant** is an intelligent document analysis and interactive chatbot powered by AI. It helps users extract key insights, analyze content, and chat about the document's information in real-time. The app supports PDF, Word, and Image files, making document processing easier and more interactive.

---

## 🛠 Features

- **Smart Document Analysis**: Extract key insights and summaries from your documents instantly.
- **Interactive Chat**: Ask questions and get intelligent responses about your document.
- **Multi-Format Support**: Works with PDF, Word, and Image files.

---

## 🚀 Getting Started

### Prerequisites
To run this project locally, you'll need:
- Python 3.7+
- `pip` (Python package installer)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/man-swi/DocuMind-AI-Assistant.git
    cd DocuMind-AI-Assistant
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Mistral API Key**:
   - Go to [Mistral](https://www.mistral.ai/) and sign up for an API key.
   - Create a `.env` file in the root directory of the project and add the following:
     ```bash
     MISTRAL_API_KEY=your_api_key_here
     ```

---

## 🖥 Running the App

1. **Start the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open the app in your browser**:
    - Go to `http://localhost:8501` to interact with the DocuMind AI Assistant.

---

## 📄 Features in Detail

### Smart Document Analysis
- Upload a document (PDF, Word, or Image), and the AI will extract key information, topics, and summaries from it.
  
### Interactive Chat
- Ask anything related to the document's content. The AI assistant will answer questions based on the document.

---

## ⚙️ Technologies Used

- **Python**: Programming language
- **Streamlit**: Framework for building interactive web apps
- **Mistral AI**: AI model used for document analysis and interaction
- **PyPDF2**: PDF extraction library
- **python-docx**: For reading Word documents
- **pytesseract**: For OCR (text extraction from images)
- **Pillow**: Image processing library

---

## 🛠 Setup Instructions for Developers

### File Structure
