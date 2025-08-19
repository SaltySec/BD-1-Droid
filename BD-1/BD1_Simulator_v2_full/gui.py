import tkinter as tk

class BD1GUI:
    def __init__(self, config):
        self.config = config
        self.root = tk.Tk()
        self.root.title("BD-1 Simulator")
        self.status = tk.StringVar(value="Say 'hey bd1'...")

        self.label = tk.Label(self.root, textvariable=self.status, font=("Arial", 16))
        self.label.pack(pady=20)

    def update_status(self, text, intent, emotion):
        self.status.set(f"Heard: {text}\nIntent: {intent}\nEmotion: {emotion}")

    def animate_emotion(self, emotion):
        print(f"[GUI] Animate: {emotion} (LED + servo sim)")

    def start(self, stt):
        self.root.after(100, stt.start)
        self.root.mainloop()
