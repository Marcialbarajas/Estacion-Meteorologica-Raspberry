import mysql.connector
import datetime
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="weather"
)


now=datetime.datetime.now()

mycursor = mydb.cursor()

sql = "INSERT INTO data (fecha, temperature, pressure, humidity) VALUES (%s, %s, %s, %s)"

val=(now.strftime('%Y-%m-%d %H:%M:%S'), "12", "31", "13")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
