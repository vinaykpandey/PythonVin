#!/usr/bin/python
import sys
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

cursor.execute("SHOW TABLES")

tdata = cursor.fetchall()
print(tdata);
#sys.exit()
for row in tdata:
  print(row);

# disconnect from server
db.close()
