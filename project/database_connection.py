import mysql.connector


def dataUpdate(name,address,zipcode,mobile,items):
'''
Connects to database and inserts the record
'''
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="",
	  database='chatbot_db'
	)

	mycursor=mydb.cursor()
	#Inserts record into requests table
	sql = "INSERT INTO requests (Name, Address, Zipcode, Mobile, Items, Status) VALUES (%s, %s, %s, %s, %s, %s);"
	val = (name, address, zipcode, mobile, items, 'Active')
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount,'record inserted')

