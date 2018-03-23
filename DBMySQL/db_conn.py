#!/usr/bin/python
'''

http://www.metaltoad.com/blog/getting-command-line-access-php-and-mysql-running-mamp-osx

i have run the command in "sudo ln -s /Applications/MAMP/tmp/mysql/mysql.sock /tmp/mysql.sock"
and able to access php+mysql in CLI


'''
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()
