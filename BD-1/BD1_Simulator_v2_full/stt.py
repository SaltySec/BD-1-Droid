import queue
import sounddevice as sd
import vosk
import json

class SpeechToText:
    def __init__(self, config):
        self.config = config
        self.on_command = None
        self.q = queue.Queue()
        self.model = vosk.Model("models/vosk/vosk-model-small-en-us-0.15")
        self.rec = vosk.KaldiRecognizer(self.model, 16000)

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.q.put(bytes(indata))

    def start(self):
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=self.audio_callback):
            while True:
                data = self.q.get()
                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    text = result.get("text", "").lower()
                    if self.config['wake_word'] in text and self.on_command:
                        command = text.replace(self.config['wake_word'], "").strip()
                        if command:
                            self.on_command(command)
