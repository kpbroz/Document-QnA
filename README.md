# RAG Application

This repository contains a simple RAG (Retrieval-Augmented Generation) application. The application allows users to upload a text document and ask questions based on its content. It uses advanced vector databases and frameworks to achieve efficient and accurate retrieval and answering.

---

## Features

- **Document Upload**: Users can upload a text document as the knowledge source.
- **Question Answering**: Ask any question about the uploaded document.
- **Vector Databases**: Utilizes FAISS and Pinecone for vector-based similarity searches.
- **LangChain Framework**: Orchestrates the retrieval and generation pipeline.
- **User Interface**: Built using Streamlit for a seamless experience.
- **Backend**: Powered by FastAPI for robust and scalable backend operations.

---

## Prerequisites

1. Python 3.8 or higher.
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file to store your API keys. Example:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## How to Run

### 1. Start the Backend
   Run the FastAPI backend server:
   ```bash
   uvicorn backend_app:app --reload
   ```

### 2. Start the Frontend
   Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the Streamlit application in your browser (Streamlit will provide the URL after starting).
2. Upload a text document.
3. Ask any question about the uploaded document in the interface.

---

## Tech Stack

- **Vector Databases**: FAISS, Pinecone
- **Framework**: LangChain
- **Backend**: FastAPI
- **Frontend**: Streamlit

---

## Notes

- Ensure the `.env` file is properly configured with your API keys before starting the application.
- The `requirements.txt` file lists all necessary dependencies.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

