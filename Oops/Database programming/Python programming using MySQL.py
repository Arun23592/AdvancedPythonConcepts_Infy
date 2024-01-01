import mysql.connector

con = mysql.connector.connect(host="host", user="username", password="password", database="database_name")
con.close()

cur.execute("SELECT * FROM Computer")
for row in cur:
    print(row)
cur.close()
con.close()
