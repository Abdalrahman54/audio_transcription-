# Audio Transcription with OpenAI Whisper
This project provides an audio transcription service using OpenAI's Whisper model. It can be used both as a Streamlit app for interactive use and as an API for programmatic integration.

Features
Upload audio files (MP3, M4A, WAV).
Transcribe audio into English text using OpenAI’s Whisper.
User-friendly interface with Streamlit for direct interaction.
API endpoint for programmatic access to the transcription service.
Installation
Prerequisites
Python 3.7+
Required libraries:
openai
streamlit
Set up OpenAI API Key
You must have an OpenAI API key to use this application. Set the OPENAI_API_KEY environment variable with your key.

Running the Streamlit App
Start the Streamlit Application
To run the Streamlit app, use the following command in your terminal:

streamlit run audio_transcription.py
Interact with the App
Upload an audio file (MP3, M4A, WAV).
Click the "Transcribe Audio" button to transcribe the audio into English text.
The transcription will be displayed on the screen.
API Usage (for programmatic access)
Function: transcribe_audio
Parameters:
audio_file: The audio file to be transcribed. Supported formats include:
MP3
M4A
WAV
Returns:
str: The transcription of the audio in English.
None: If an error occurs during transcription.
