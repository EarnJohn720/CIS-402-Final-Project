import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_SQL2021"
)

print(mydb)
