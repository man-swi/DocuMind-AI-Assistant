# DocuMind AI Assistant

📚 **DocuMind AI Assistant** is an intelligent document analysis and interactive AI chatbot that helps users extract key insights, analyze content, and ask questions about the document's information in real-time. The app supports PDF, Word, and Image files, making document processing easier and more interactive.

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
   ![Chatbot Interface](path_to_image/chatbot_interface.png)

2. **Extracted Text**:  
   This image displays the extracted text from a document, providing insights and summaries to the user.  
   ![Extracted Text](path_to_image/extracted_text.png)

3. **Settings Option**:  
   This screenshot shows the settings section where users can print the output or change the theme of the assistant interface.  
   ![Settings Option](path_to_image/settings_option.png)

4. **Chat Feature with Save/Download**:  
   This image shows the chat section where users can ask questions, and the assistant can save the conversation data for later download or printing.  
   ![Chat Feature](path_to_image/chat_feature.png)

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

---

