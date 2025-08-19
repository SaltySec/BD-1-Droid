import subprocess
import json

class OllamaLLM:
    def __init__(self, config):
        self.model = config['ollama_model']
        self.config = config

    def interpret(self, text):
        prompt = f"User command: '{text}'. Respond with a JSON object: {{intent: string, emotion: one of {list(self.config['emotions'].keys())}}}."
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt.encode(),
                capture_output=True,
                check=True
            )
            output = result.stdout.decode().strip()
            data = json.loads(output)
            return data.get("intent", "unknown"), data.get("emotion", self.config['fallback_emotion'])
        except Exception as e:
            print("[LLM error]", e)
            return "unknown", self.config['fallback_emotion']
