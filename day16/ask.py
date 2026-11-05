import requests
URL="http://localhost:11434/api/chat"
Model="llama3.1:8b"
def ask(question,system=None):
    messages=[]
    if system:
        messages.append({"role" : "system", "content": system})
    messages.append({"role" : "user", "content": question})
    payload={"model": Model,"messages": messages,"stream":False}
    response=requests.post(URL,json=payload,timeout=120)
    response.raise_for_status()
    return response.json()["message"]["content"]

question = "What does ORA-99999 mean? Answer in two sentences."
system_msg = "You are an Oracle DBA assistant. Answer briefly. If you are not sure, say you don't know."

try:
    print("RUN 1 (no system message):")
    print(ask(question))
    print()
    print("RUN 2 (with system message):")
    print(ask(question, system=system_msg))
except requests.RequestException as e:
    print("Problem:", type(e).__name__)

    