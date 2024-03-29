
from flask import Flask, request, jsonify
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import whisper
import os
from flask_cors import CORS
from openai import OpenAI

# from flask_socketio import SocketIO, send
# from vosk import Model, KaldiRecognizer
import pyaudio


app = Flask(__name__)
CORS(app)  
# socketio = SocketIO(app, cors_allowed_origins="*")

print("Loading  model...")
model = whisper.load_model("medium")
print(" Model loaded.")

client = OpenAI(
    api_key='',
)


@app.route('/clinical-note-generation', methods=['POST'])
def generate_clinical_note():
    # Get the transcription from the request data
    transcription = request.json.get('transcription')
    print("Transcription:")
    print(transcription)

    # Define the questions for the clinical note
    questions = """
    Given the transcription of a doctor-patient conversation, answer the following questions to complete the clinical note:

    1. Patient Name and Age: What is the patient's name and age?
    2. Chief complaint: What is the patient's chief complaint?
    3. History of present illness: Can you describe the nature, severity, radiation, duration of the patient's symptoms, and any aggravating or relieving factors?
    4. Dental visit frequency: How often has the patient visited a dentist?
    5. Radiation treatment: Has the patient received radiation treatment for the head and neck?
    6. Medication usage: What medications is the patient currently taking, both for the chief complaint and other reasons?
    7. Dry mouth: Does the patient often have a dry mouth?
    8. Dietary habits: What are the patient's habits regarding tobacco, sugar, snacks, bakery items, or soft drinks?
    9. Other health complications: Does the patient have any other health complications or serious illnesses?
    10. Chewing discomfort: Does the patient experience pain when chewing?
    11. Tooth and gum issues: Does the patient frequently have toothaches, gum pain, or gum bleeding?
    12. Oral discomfort: Does the patient experience burning in the mouth or pain in the jaw or neck?
    13. Dental care products: What kind of toothbrush and toothpaste does the patient use?
    14. Family history of dental caries: Is there a family history of dental caries?
    """

    # Create the prompt for GPT-3.5-turbo
    prompt = questions + "\nTranscription:\n" + transcription

    # Generate the clinical note using GPT-3.5-turbo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    # Get the generated text from the response
    generated_text = response.choices[0].message.content

    print("Generated clinical note:")
    print(generated_text)

    # Return the generated clinical note
    return jsonify({'clinical_note': generated_text})
    # return jsonify({'clinical_note': "Hello"})




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


