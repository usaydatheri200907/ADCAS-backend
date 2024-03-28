# from flask import Flask, request, jsonify
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
# import whisper
# import os
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Add CORS support to your Flask app

# # Load the Whisper model (choose the appropriate size, e.g., 'large')
# model = whisper.load_model("large-v2")

# def transcribe_audio():
#     # Assuming the audio file is in the same directory as the script
#     audio_file_path = "1.mp4"  # Use a relative path

#     # Check if the audio file exists
#     if not os.path.exists(audio_file_path):
#         print(f"Audio file not found: {audio_file_path}")
#         return

#     # Transcribe the audio
#     transcription = model.transcribe(audio_file_path, language='EN')
#     # transcription = "hello"

#     # Print the transcription
#     print("Transcription:")
#     print(transcription)
#     with open("transcribed_text.txt", "w") as f:
#         f.write(transcription["text"])

#     return jsonify({'transcription': transcription["text"]})

# if __name__ == '__main__':
#     with app.app_context():  # Establish application context
#         app.run(host='localhost', port=3001)
#         transcribe_audio()


from flask import Flask, request, jsonify
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import whisper
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add CORS support to your Flask app

print("Loading Whisper model...")
# Load the Whisper model (choose the appropriate size, e.g., 'medium')
model = whisper.load_model("medium")
print("Whisper model loaded.")

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
    app.run(host='localhost', port=3001)
    print("Flask server started.")
