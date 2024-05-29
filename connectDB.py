import mysql.connector
import mariadb

try:
    connection = mysql.connector.connect(host="0.tcp.jp.ngrok.io", port=15305, user="411062002", password="411062002", database="411062002")
except mysql.connector.Error as e:
    print("Error: Could not make connection to the MySQL database")
    print(e)
cursor = connection.cursor()
query = "select * from vehicle;"
cursor.execute(query)
for db in cursor:
    print(db)
cursor.close()
connection.close()