import mysql.connector


def dataUpdate(name,address,zipcode,mobile,items):

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="anil1234",
	  database='chatbot_db'
	)

	mycursor=mydb.cursor()
	sql = "INSERT INTO requests (Name, Address, Zipcode, Mobile, Items, Status) VALUES (%s, %s, %s, %s, %s, %s);"
	val = (name, address, zipcode, mobile, items, 'Active')
	mycursor.execute(sql, val)
	# sql=f'INSERT INTO requests (Name, Address, Mobile_num, Request, Status) values ({name},{address},{mobile},{items},'Active');'
	# mycursor.execute(sql)
	mydb.commit()
	print(mycursor.rowcount,'record inserted')

# if __name__=='__main__':
# 	dataUpdate('Test_name_python','test_address_python','test_mobile_python','test_items_python')
