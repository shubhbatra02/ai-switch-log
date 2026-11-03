import requests
url = "http://localhost:11434/api/chat"

payload = { "model": "llama3.2",
           "messages": [{"role": "user", "content": "What does ORA-01555 mean? Answer in two sentences."}],
           "stream": False}

try:
     response = requests.post(url,json=payload,timeout=120)
     response.raise_for_status()
     data = response.json()
     print(list(data.keys()))
     print(data["message"]["content"])
except requests.RequestException as e:
    print(f"Problem: {type(e).__name__}")
