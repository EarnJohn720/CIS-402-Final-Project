import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_SQL2021",
  database="menagerie"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE menagerie")
#mycursor.execute("DROP DATABASE menagerie")
#mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
mycursor.execute("DESCRIBE pet")
for x in mycursor:
  print(x)


