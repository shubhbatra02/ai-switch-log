import oracledb
import os
connection = oracledb.connect(user="system",password=os.environ["DB_PASSWORD"],dsn="localhost:1521/FREEPDB1")
cursor=connection.cursor()
cursor.execute("select 'X' from dual")
print(cursor.fetchone())
cursor.execute("select banner_full from v$version")
print(cursor.fetchone())
cursor.execute("select username, created from all_users order by created")
for row in cursor:
 print(row)
connection.close()


