def double(n):
    return n * 2


number= int(input("Enter a number: "))
result = double(number)
print(f"The double of {number} is {result}")


sentence=("The brown fox jumps over the lazy dog and the dog jumps over the brown lion")
words=sentence.lower().split()

def word_count(words):
    counter={}
    for word in words:
        counter[word] = counter.get(word, 0) + 1        
    return counter

word_counts = word_count(words)
for result in word_counts:
    print(f"{result} : {word_counts[result]}")



def check_number(n):
    if n > 50:
        return "The number is greater than 50."
    elif n < 50:
        return "The number is less than 50."
    else:
        return "The number is equal to 50."


num=int(input("Enter a number to check: " ))
result=check_number(num)
print(result)