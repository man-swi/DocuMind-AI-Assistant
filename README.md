# DocuMind AI Assistant

📚 **DocuMind AI Assistant** is an intelligent document analysis and interactive AI chatbot that helps users extract key insights, analyze content, and ask questions about the document's information in real-time. This project employs a **Retrieval-Augmented Generation (RAG)** approach, enabling it to provide accurate and contextually relevant responses by combining document retrieval and AI-generated answers. The app supports PDF, Word, and Image files, making document processing easier and more interactive.

---

## 🛠 Features

- **Smart Document Analysis**: Instantly extract key insights, summaries, and important content from your documents.
- **Interactive Chat**: Ask questions and receive intelligent, context-based answers directly from the document.
- **Multi-Format Support**: Supports PDF, Word, and Image files for versatile document processing.

---

## 🚀 Getting Started

To get the **DocuMind AI Assistant** up and running on your local machine, follow these steps:

### Prerequisites

Ensure you have the following installed:
- **Python 3.7+** 
- **pip** (Python package installer)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/man-swi/DocuMind-AI-Assistant.git
    cd DocuMind-AI-Assistant
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API Key**:
    - Obtain your API key by signing up at [Mistral AI](https://www.mistral.ai/).
    - Create a `.env` file in the project root directory and add your Mistral API key:
      ```bash
      MISTRAL_API_KEY=your_api_key_here
      ```

---

## 🖥 Running the App

To launch the **DocuMind AI Assistant** locally, follow these steps:

1. **Start the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open the app in your browser**:
    - Go to [http://localhost:8501](http://localhost:8501) to interact with the **DocuMind AI Assistant**.

---

## 📄 Features in Detail

### Smart Document Analysis
- Upload a document (PDF, Word, or Image) and let the AI extract key insights, important topics, and summaries. The assistant processes text, images, and more to provide meaningful analysis.

### Interactive Chat
- Engage with the assistant by asking questions about the document’s content. The AI will respond intelligently, providing answers based on the document's contents.

---

## 🖼 Project Screenshots

Here are some screenshots showing how the **DocuMind AI Assistant** works:

1. **Chatbot Interface**:  
   This image shows the main interface where the chatbot assistant interacts with the user. It’s the place where all conversations happen.  
   ![documind](https://github.com/user-attachments/assets/5bda6293-31ba-42d6-8cc7-5dba474ad54a)

2. **Extracted Text**:  
   This image displays the extracted text from a document, providing insights and summaries to the user.  
   ![extracted](https://github.com/user-attachments/assets/e6d548fd-8bb9-4f3d-86e6-8f35efc12e53)

3. **Settings Option**:  
   This screenshot shows the settings section where users can print the output or change the theme of the assistant interface.  
   ![settings](https://github.com/user-attachments/assets/eede0b43-3a29-4944-ae74-3a0749617c37)

4. **Chat Feature with Save/Download**:  
   This image shows the chat section where users can ask questions, and the assistant can save the conversation data for later download or printing.  
   ![chat answers](https://github.com/user-attachments/assets/6bf63eb8-4f8e-4c97-bb5a-1c9bca570ec4)

---

## ⚙️ Technologies Used

This project uses a combination of technologies to build the interactive and intelligent document assistant:

- **Python**: Core programming language.
- **Streamlit**: Framework for building interactive, web-based applications.
- **Mistral AI**: The AI model responsible for document analysis and real-time interaction.
- **PyPDF2**: Library for PDF text extraction.
- **python-docx**: Library to read and extract data from DOCX files.
- **pytesseract**: Optical Character Recognition (OCR) tool for extracting text from images.
- **Pillow**: Image processing library used for handling and manipulating images.
- **FAISS**: Library for efficient similarity search and clustering of dense vectors.

---

## 🌐 Deployed App

You can access the live version of **DocuMind AI Assistant** here:  
[DocuMind AI Assistant - Streamlit App](https://man-swi-documind-ai-assistant-app-fodyzu.streamlit.app/)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
