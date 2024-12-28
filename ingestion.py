import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS

load_dotenv()

def upload_to_database(file_path):
    print("starting data ingestion......")
    
    loader = TextLoader(file_path=file_path,
        encoding="utf-8")
    document = loader.load()
    
    print("splitting....")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"Created {len(texts)} chunks")
    
    embeddings =  OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    
    print("ingesting....")
    
    # using pinecone
    # PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ["INDEX_NAME"])
    
    # using FAISS in-memory vector DB
    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local("faiss_document_qna")
    print("finish")
    
    
    