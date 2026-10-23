from pathlib import Path

counter=0
try:
 with open("day5/sample2.log","r",encoding="utf-8") as f:

    for line in f:
        if "ERROR" in line:
            counter+=1

except FileNotFoundError:
    print("The log file does not exist.") 

print (f" Total number of errors in the log file is {counter} ")