import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = 3306,
    auth_plugin='mysql_native_password'

)

# prepare cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')