from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os

from ingestion import upload_to_database
from answer_retriever import answer_query

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIRECTORY = "uploaded_files"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/upload-txt/")
async def upload_txt_file(file: UploadFile = File(...)):
    # Check if the file is a .txt file
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")

    # Define the file path where the file will be stored
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    try:
        # Write the file to local storage
        with open(file_path, "wb") as f:
            f.write(await file.read())
            
        upload_to_database(file_path)
        return JSONResponse(content={"message": "File uploaded successfully", "file_path": file_path})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask-me/")
async def ask_me(request: QuestionRequest):
    result = answer_query(request.question)
    return {"response": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
