
from flask import Flask, request, jsonify
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import whisper
import os
from flask_cors import CORS
# from flask_socketio import SocketIO, send
# from vosk import Model, KaldiRecognizer
import pyaudio


app = Flask(__name__)
CORS(app)  # Add CORS support to your Flask app
# socketio = SocketIO(app, cors_allowed_origins="*")

print("Loading Whisper model...")
# Load the Whisper model (choose the appropriate size, e.g., 'medium')
model = whisper.load_model("medium")
print("Whisper model loaded.")

# print("Loading Vosk model...")
# model = Model("D:\\FYP\\AudioPage\\ADCAS-backend\\Vosk\\vosk-model-small-en-in-0.4")
# print("Loading recognizer...")
# recognizer = KaldiRecognizer(model, 16000)
# print("Loading mic...")
# mic = pyaudio.PyAudio()
# print("Initializing stream...")
# stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
# print("Starting stream...")
# stream.start_stream()



# @socketio.on('audio', namespace='/realtime')
# def handle_audio(audio_data):
#     if recognizer.AcceptWaveform(audio_data):
#         result = json.loads(recognizer.Result())
#         emit('transcription', {'transcription': result['text']}, namespace='/realtime')



def transcribe_audio(audio_file_path):
    print(f"Transcribing audio file: {audio_file_path}")
    # Check if the audio file exists
    if not os.path.exists(audio_file_path):
        print(f"Audio file not found: {audio_file_path}")
        return jsonify({'error': 'Audio file not found'})

    # Transcribe the audio
    print("Transcribing...")
    transcription = model.transcribe(audio_file_path, language='EN')

    # Print the transcription
    print("Transcription:")
    print(transcription)
    with open("transcribed_text.txt", "w") as f:
        f.write(transcription["text"])

    print("Transcription completed.")
    return jsonify({'transcription': transcription["text"]})

@app.route('/transcribe', methods=['POST'])
def transcribe_endpoint():
    print("Received POST request at /transcribe endpoint.")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    audio_file = request.files['file']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        audio_file_path = "uploaded_audio.mp4"
        audio_file.save(audio_file_path)
        print(f"Saved uploaded file to: {audio_file_path}")
        return transcribe_audio(audio_file_path)


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='localhost', port=5000)
    print("Flask server started.")
