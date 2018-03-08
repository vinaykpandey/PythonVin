#!/usr/bin/python2.7

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
#for row in tdata:
 #  print(row);


cursor.execute("SELECT  *  FROM `team_name` ")
tdata = cursor.fetchall()

for row in tdata:
    print(type(row))
    print(row);

#sys.exit()
#insert in to team_name
sql = "INSERT INTO `team_name`  SET `scores` = 'Abc' , `email` = 'abc@gmail.com' "
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in
 db.rollback()

# disconnect from server
db.close()
