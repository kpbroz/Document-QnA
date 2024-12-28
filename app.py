import streamlit as st
import requests

# Backend API URLs
UPLOAD_API_URL = "http://localhost:8000/upload-txt/"
ASK_API_URL = "http://localhost:8000/ask-me/"

# Load external CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load and apply the CSS
load_css("styles.css")

# Add the title
st.markdown('<h1 class="title">Bale Kenle!</h1>', unsafe_allow_html=True)

# File Upload Section
st.header("Upload a Text File")
uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

if st.button("Upload File"):
    if uploaded_file is not None:
        try:
            # Send the file to the upload-txt API
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(UPLOAD_API_URL, files={"file": uploaded_file})
            
            if response.status_code == 200:
                st.success("File uploaded successfully!")
                st.json(response.json())
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a file before clicking 'Upload File'.")

# Question Section
st.header("Ask a Question")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question.strip():
        try:
            # Send the question to the ask-me API
            response = requests.post(ASK_API_URL, json={"question": question})
            
            if response.status_code == 200:
                answer = response.json().get("response", "No response")
                st.success("Answer Retrieved!")
                st.write(f"**Answer:** {answer}")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before clicking 'Get Answer'.")

