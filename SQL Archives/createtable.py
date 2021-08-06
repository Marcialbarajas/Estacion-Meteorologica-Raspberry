import mysql.connector

mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="weather"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE data(id INT(11) NOT NULL AUTO_INCREMENT, date DATETIME, temperature VARCHAR(255), pressure VARCHAR(255), humidity VARCHAR(255), altitude VARCHAR(255), wind VARCHAR(255), rain VARCHAR(255), PRIMARY KEY(id))")
