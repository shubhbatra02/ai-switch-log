import oracledb
import os

connection= oracledb.connect(user=os.environ.get("DB_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             dsn=os.environ.get("DB_DSN"),
                             tcp_connect_timeout=10
                             )
cursor=connection.cursor()

cursor.execute("Select 'hello from inside container'   from dual")
print(cursor.fetchone())
connection.close()
