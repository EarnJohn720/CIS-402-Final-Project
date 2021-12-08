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
#mycursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)")
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#  print(x)
#mycursor.execute("DESCRIBE pet")
#for x in mycursor:
#  print(x)

sql = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
  ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', None),
  ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', None),
  ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', None),
  ('Fang', 'Benny', 'dog', 'm', '1990-08-27', None),
  ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'),
  ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', None),
  ('Whistler', 'Gwen', 'bird', None, '1997-12-09', None),
  ('Slim', 'Benny', 'snake', 'm', '1996-04-29', None)
]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM pet")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)