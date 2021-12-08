import re
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_SQL2021",
  database="menagerie"
)

pet_names = []
birth_dates = []
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM pet")
myresult = mycursor.fetchall()
#re.search('[a-zA-Z]', the_string)
for x in myresult:
    pet_names.append(str(x))

mycursor.execute("SELECT birth FROM pet")
myresult = mycursor.fetchall()
for x in myresult:
    birth_dates.append(str(x))
mycursor.execute("SELECT COUNT(*) FROM pet")
NumOfPets = int(mycursor.fetchone()[0])

print("Names                     Birth Date")
print("------------------------------------")
#"{:<15}{:^10}{:>15}".format(left_aligned, center, right_aligned)
for x in range(NumOfPets):
   print("{:<18}{:>18}".format(pet_names[x], birth_dates[x]))
#temp = ''
#temp2 = ''
#pets = []
#for x in pet_names:
#    temp = x
#    for y in temp:
#        if y.isalpha() == True:
#            temp2 += y
#    pets.append(temp2)
#    temp2 = ''


#Step 23
#mycursor.execute("SELECT COUNT(*) FROM pet")
#NumOfPets = mycursor.fetchone()[0]

#print("You have", NumOfPets + 1, "pets.")
#Step 21
#mycursor = mydb.cursor()

#mycursor.execute("SELECT name, birth FROM pet")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)
#Step 18
#mycursor = mydb.cursor()
#sql = "SELECT * FROM pet WHERE sex ='f'"

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)


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
#Step 14
#sql = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)"
#val = [
#  ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', None),
#  ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', None),
#  ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', None),
#  ('Fang', 'Benny', 'dog', 'm', '1990-08-27', None),
#  ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'),
#  ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', None),
#  ('Whistler', 'Gwen', 'bird', None, '1997-12-09', None),
#  ('Slim', 'Benny', 'snake', 'm', '1996-04-29', None)
#]

#mycursor.executemany(sql, val)

#mydb.commit()
#print(mycursor.rowcount, "was inserted.")

#mycursor.execute("SELECT * FROM pet")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)