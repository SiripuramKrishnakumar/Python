import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",port="3308",user="kittu",passwd="kittu",database="testdb")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

# data =  mycursor.fetchall()

# for i in data:
#	print(i)

student = mycursor.fetchone()

print(student)


