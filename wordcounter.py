sentence=("The brown fox jumps over the lazy dog and the dog jumps over the brown lion")
counter={}
words=sentence.lower().split()
for word in words:
    #if word in counter:
     #   counter[word]=counter[word]+1
    #else:
        #counter[word]=1
   counter[word] = counter.get(word, 0) + 1        

for result in counter:
    print(f"{result} : {counter[result]}")