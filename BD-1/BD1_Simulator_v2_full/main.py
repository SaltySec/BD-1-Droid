import yaml
import tkinter as tk
from gui import BD1GUI
from stt import SpeechToText
from llm import OllamaLLM
from audio import AudioEngine

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    gui = BD1GUI(config)
    stt = SpeechToText(config)
    llm = OllamaLLM(config)
    audio = AudioEngine(config)

    def process_command(text):
        intent, emotion = llm.interpret(text)
        gui.update_status(text, intent, emotion)
        audio.play_emotion(emotion)
        gui.animate_emotion(emotion)

    stt.on_command = process_command

    gui.start(stt)

if __name__ == "__main__":
    main()
