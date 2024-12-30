import streamlit as st
import openai
import os

# Set OpenAI API Key
openai.api_key = "API key"  # Replace with your OpenAI API key

def transcribe_audio(audio_file):
    """
    Transcribe the uploaded audio file and return the transcription using OpenAI's Whisper.

    Parameters:
    - audio_file (UploadedFile): The audio file uploaded by the user. The file can be in mp3, m4a, or wav format.
    
    Returns:
    - str: The transcription of the uploaded audio file in English.
    - None: If transcription fails or an error occurs.
    """
    try:
        # Open and transcribe the audio file using Whisper with language set to English
        response = openai.Audio.transcribe("whisper-1", audio_file, language="en")
        transcription = response["text"]

        return transcription

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        return None

# Streamlit UI
st.title("Audio Transcription with OpenAI Whisper")

# Upload audio file
audio_file = st.file_uploader("Upload your audio file (mp3, m4a, wav)", type=["mp3", "m4a", "wav"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")

    # Transcribe audio when button is pressed
    if st.button("Transcribe Audio"):
        st.info("Transcribing your audio... please wait.")
        transcription = transcribe_audio(audio_file)

        if transcription:
            st.subheader("Transcription")
            st.write(transcription)

        else:
            st.error("An error occurred during transcription.")
