
from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_audio():
    try:
        audio = request.files['audio']
        audio_path = 'uploads/' + audio.filename
        audio.save(audio_path)

        model = Model("model")
        wf = wave.open(audio_path, 'rb')
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()

        result = json.loads(result)
        transcript = result['text']
        os.remove(audio_path)

        return jsonify({'transcript': transcript})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to convert audio'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
