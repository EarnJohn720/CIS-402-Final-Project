import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_SQL2021"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE menagerie")
#mycursor.execute("DROP DATABASE menagerie")


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

