import os, random
import pygame

class AudioEngine:
    def __init__(self, config):
        self.config = config
        pygame.mixer.init()

    def play_emotion(self, emotion):
        folder = self.config['emotions'].get(emotion, self.config['fallback_emotion'])
        path = os.path.join("sounds", folder)
        if not os.path.exists(path):
            print(f"[Audio] Missing folder: {path}")
            return
        files = [f for f in os.listdir(path) if f.endswith('.wav') or f.endswith('.mp3')]
        if not files:
            print(f"[Audio] No files in {path}")
            return
        file = random.choice(files)
        full_path = os.path.join(path, file)
        print(f"[Audio] Playing {full_path}")
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play()
