from pathlib import Path

def readora(path):
 counter={}

 with open("day6/sample.log","r",encoding="utf-8") as f:
        for line in f:
            if "ORA-" in line:
                #This is code for extracting Ora error full line
                #print(line)
                #This code is used when ORA error are exactly at starting nothing is there before them
                #errorcode=line.split(":")[0]
                #print(errorcode)
                #This code is used when ORA error are not exactly at starting something is there before them
                start= line.find("ORA-") #This will find atrating position of Ora error
                errorcode=line[start:start+9] #This will help in slicing ora error code like Ora-+ charcters
                print(errorcode)
                # To count the number of each error code in the log file
                counter[errorcode]=counter.get(errorcode,0)+1
 return counter


try:
     log_path=Path(__file__).parent / "sample.log"
     counter = readora(log_path)
except FileNotFoundError:
    print("The log file doesnot exist.")
else:
##Sort and print (10 min): sorted(counter.items(), key=lambda x: x[1], reverse=True) gives highest count first. Don’t worry if the lambda looks odd, copy it and ask me what it does afterwards.
 sorted_errors = sorted(counter.items(), key=lambda x: x[1], reverse=True)
 print("Sorted error codes by count (highest first):")
 for error_code, count in sorted_errors:
    print(f"{error_code}: {count}")
         