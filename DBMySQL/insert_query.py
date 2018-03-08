#!/usr/bin/python
import sys
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","test" )
# prepare a cursor object using cursor() method
cursor = db.cursor() #

sql = "INSERT INTO `team_name`  SET `scores` = '50' , `email` = 'abc@gmail.com' "
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
