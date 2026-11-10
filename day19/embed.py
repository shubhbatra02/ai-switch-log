import requests
import json
import math
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

query=embed("my long query failed because of insufficient undo space")
print(query[0:5])





def cosine(a,b):
    dotproduct= sum(x * y for x,y in zip(a,b))
    len_a=math.sqrt(sum(x**2 for x in a))
    len_b=math.sqrt(sum(y**2 for y in b))
    if len_a == 0 or len_b == 0:
        return 0.0
    return dotproduct/(len_a*len_b)


for result in results:
    print(cosine(result,query))
#result=embed("my long query failed because undo was overwritten")
#print(len(result))
#print(result[0:5])