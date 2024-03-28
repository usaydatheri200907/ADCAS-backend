from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import whisper
import os

print("Importing modules... Done.")

# Load the Whisper model (choose the appropriate size, e.g., 'large')
print("Loading Whisper model...")
model = whisper.load_model("medium")
print("Whisper model loaded.")

def transcribe_audio():
    # Use an absolute path for the audio file
    audio_file_path = r"C:\Users\aliar\Documents\awais\server\assets\1.mp4"

    # Check if the audio file exists
    print(f"Checking if audio file exists at: {audio_file_path}")
    try:
        with open(audio_file_path, 'rb') as f:
            print(f"Audio file found: {audio_file_path}")
    except FileNotFoundError:
        print(f"Audio file not found: {audio_file_path}")
        return

    print("Audio file found. Transcribing...")
    # Transcribe the audio
    transcription = model.transcribe(audio_file_path, language='EN')

    # Print the transcription
    print("Transcription:")
    print(transcription)
    with open("transcribed_text.txt", "w") as f:
        f.write(transcription["text"])

print("RUNNING")
transcribe_audio()
