import openai
import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

# Set OpenAI API Key
openai.api_key = "API key"  # Replace with your OpenAI API key

# Initialize FastAPI app
app = FastAPI()

# Supported audio formats
ALLOWED_AUDIO_FORMATS = {"mp3", "wav", "m4a"}

class TranscriptionResponse(BaseModel):
    transcription: str
    error: str = None

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribe audio using OpenAI Whisper and return the transcription.

    Parameters:
    - audio_file (BinaryIO): The audio file to be transcribed. It should be in one of the supported formats (mp3, m4a, wav).
    
    Returns:
    - str: The transcription of the audio in English.
    - None: If an error occurs during transcription.
    """
    try:
        # Check if the uploaded file is of an allowed format
        file_extension = file.filename.split('.')[-1].lower()
        if file_extension not in ALLOWED_AUDIO_FORMATS:
            raise HTTPException(status_code=400, detail="Invalid file format. Allowed formats are: mp3, wav, m4a.")

        # Save the uploaded file to a temporary location
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            shutil.copyfileobj(file.file, temp_file)

        # Transcribe the audio file using Whisper
        with open(temp_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file, language="en")
            transcription = response["text"]

        # Clean up the temporary file
        os.remove(temp_file_path)

        return TranscriptionResponse(transcription=transcription)

    except HTTPException as e:
        raise e
    except Exception as e:
        # General exception handler
        return JSONResponse(
            status_code=500,
            content={"error": f"An internal error occurred: {str(e)}"}
        )

