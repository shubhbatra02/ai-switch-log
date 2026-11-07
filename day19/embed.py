import requests
import json

url="http://localhost:11434/api/embed"
model="embeddinggemma-2:latest"

def embed(text):
    payload={"model":model,"input":text}
    response=requests.post(url,json=payload,timeout=120)
    response.raise_for_status()
    data=response.json()
    return data["embeddings"][0]
    #print(list(data.keys()))
    #print(type(data["embeddings"]))
    #print(len(data["embeddings"]))
    #print(len(data["embeddings"][0]))




notes=["ORA-01555: snapshot too old, a long query needed undo data that was overwritten","ORA-00060: deadlock detected, two sessions waiting on each other’s locks","RMAN: Oracle’s backup and recovery tool"]
results=[]
for note in notes:
  
    result=embed(note)
    results.append(result)

print (len(results))
print(len(results[0]))
print(len(results[1]))
print(len(results[2]))
print(results[0][0:5])
print(results[1][0:5])
print(results[2][0:5])

query=embed("my long query failed because undo was overwritten")
print(query[0:5])


#result=embed("my long query failed because undo was overwritten")
#print(len(result))
#print(result[0:5])