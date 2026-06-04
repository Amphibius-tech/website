import os
from ollama import Client
from dotenv import load_dotenv

load_dotenv()

ollama_api_key = os.getenv("OLLAMA_API_KEY")

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + f"{ollama_api_key}"}
)

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

for part in client.chat('qwen3.5', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)