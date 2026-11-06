import requests
import json

url="http://localhost:11434/api/chat"
model="llama3.1:8b"

def ask(question):
    messages=[]
    messages.append({"role":"user","content":question})
    payload={"model":model,"messages":messages,"stream":False}
    response=requests.post(url,json=payload,timeout=120)
    response.raise_for_status()
    return response.json()["message"]["content"]

questions = [
    {"question": "what does ora-01555 mean?", "expected": "snapshot too old: a long query needed undo data that was overwritten"},
    {"question": "what does ora-06000 mean?", "expected": "an internal error, usually a bug or corruption, with the first argument identifying the condition)"},
    {"question": "what does ora-09999 mean?", "expected": "a non-documented code, so the right answer is that the model doesn’t know"},
    # your other questions here, same shape
]
try:
 results=[]
 for q in questions:
    answer=ask(q["question"])

    data_to_save={
       "question":q["question"],
       "expected":q["expected"],
       "model":model,
       "answer":answer
    }
    results.append(data_to_save)
 with open("day17/results.json","w",encoding="utf-8") as f:
       json.dump(results, f,indent=4)

 with open("day17/results.json","r",encoding="utf-8") as f:
       data=json.load(f)
       print(data)
except requests.RequestException as e:
    print("Error", type(e).__name__)

except (KeyError,TypeError) as e:
   print("Error", type(e).__name__)


