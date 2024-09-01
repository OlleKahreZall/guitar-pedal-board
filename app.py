# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

import pyaudio
import wave
import asyncio
from flask import Flask, render_template, request, Response

app = Flask(__name__)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

audio_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate():
        global audio_data
        while True:
            if audio_data:
                yield (b'--frame\r\n'
                       b'Content-Type: audio/wav\r\n\r\n' + audio_data.pop(0) + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

async def audio_loopback():
    global audio_data
    p = pyaudio.PyAudio()
    stream_in = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
    stream_out = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True)
    while True:
        data = stream_in.read(CHUNK)
        stream_out.write(data)
        audio_data.append(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(audio_loopback())
    app.run(debug=True, threaded=True)
