
oracle_versions=['11g', '12c', '18c', '19c', '21c','23ai']

for version in oracle_versions:
    print(f"Oracle database version is {version}")


role={"db01": "primary","db02":"secondary","db03":"tertiary"}
for key,value in role.items():
    print(f"Database {key} is {value}")


number= int(input("Enter a number : "))
if number > 50:
    print("The number is greater than 50")
elif number < 50:
    print("The number is less than 50")
else:
    print("The number is equal to 50")