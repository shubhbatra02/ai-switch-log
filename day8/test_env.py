import os
import oracledb
from dotenv import load_dotenv

load_dotenv()
#cursor.execute("""
#create table employees (
#       id number primary key,
#        name varchar2(50),
#        role varchar2(50),
#        salary number
#    )
#""")
#print("Table created successfully.")
#####Data insertion####
#rows = [
#     (1, "Asha", "DBA", 37),
#    (2, "Ravi", "Developer", 30),
#    (3, "Meera", "Architect", 55),
#]

#cursor.executemany("Insert into employees (id,name,role,salary) values (:1,:2,:3,:4)",rows)
#connection.commit()
#print("Data inserted successfully.")

#######selecting the table########
#cursor.execute("select id,name,role,salary from employees order by salary desc")
#for row in cursor:
#    print(row)


#######updating the table#########
#cursor.execute(" update employees set salary=:1 where name=:2",(60,"Asha"))
#connection.commit()
#print(cursor.rowcount, "record(s) updated successfully.")

#####deleting the record from the table#####
#cursor.execute("delete from employees where id=:1",(2,))
#print(cursor.rowcount, "record(s) deleted successfully.")

### to check what a list is, what a tuple is and what an item is
#cursor.execute("select id,name,role,salary from employees order by salary desc")
#rows=cursor.fetchall()
#print(rows)
#print(rows[0])
#print(rows[0][1])

#####function to insert data into the table#####
def add_employee(conn,id,name,role,salary):
    cursor=conn.cursor()
    cursor.execute("Insert into employees(id,name,role,salary) values(:1,:2,:3,:4)",(id,name,role,salary))
    conn.commit()
    print(cursor.rowcount, "record(s) inserted successfully.")
    

#####function to select data from the table#####
def get_employess(conn):
    cursor=conn.cursor()
    cursor.execute("select id,name,role,salary from employees order by salary desc")
    rows=cursor.fetchall()
    return rows  

## function for updating the table
def update_employee(conn,name,salary):
    cursor=conn.cursor()
    cursor.execute("update employees set salary=:1 where name=:2",(salary,name))
    conn.commit()
    print(cursor.rowcount, "record(s) updated successfully.")  

### fucntion to delete the record from the table
def delete_employee(conn,id):
    cursor=conn.cursor()
    cursor.execute("delete from employees where id=:1",(id,))
    conn.commit()
    print(cursor.rowcount, "record(s) deleted successfully.")


####cteating connection and calling functions
connection= oracledb.connect(user=os.environ.get("DB_USER"),password=os.environ.get("DB_PASSWORD"),dsn=os.environ.get("DB_DSN"))
add_employee(connection,4,"Ramesh","Tester",25)
update_employee(connection,"Ramesh",45)
for id,name,role,salary in get_employess(connection):
    print(f"ID: {id}, Name: {name}, Role: {role}, Salary: {salary}")
delete_employee(connection,4)
get_employess(connection)
connection.close()