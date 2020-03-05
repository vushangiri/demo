import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="Sijan",passwd="hangover35",database="Sijan")


mycursor = mydb.cursor()

mycursor.execute("select * from student")
result=mycursor.fetchone()
for i in mycursor:
    print(i)
print("change")
print("change1")
