import math

def cosine(a,b):
    dotproduct= sum(x * y for x,y in zip(a,b))
    len_a=math.sqrt(sum(x**2 for x in a))
    len_b=math.sqrt(sum(y**2 for y in b))
    if len_a == 0 or len_b == 0:
        return 0.0
    return dotproduct/(len_a*len_b)

print(cosine([1, 2, 3], [4, 5, 6])) 
print(cosine([1, 2, 3], [1, 2, 3]))
print(cosine([1, 0], [0, 1]))    