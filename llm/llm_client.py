from config import OLLAMA_URL, MODEL_NAME
import requests

def generate_response(prompt):
    response = requests.post(
        OLLAMA_URL,
        json = {
            "model" : MODEL_NAME,
            "prompt" : prompt,
            "stream" : False
        }
    )
    return response.json()["response"]