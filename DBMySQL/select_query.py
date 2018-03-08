#!/usr/bin/python
'''
return data from select query is tuple
'''
import sys
import MySQLdb
import MySQLdb.cursors #[by default cursor is  db.cursor(tuble DS)]
# Open database connection
db = MySQLdb.connect("localhost","root","root","test" )
# prepare a cursor object using cursor() method
#cursor = db.cursor() # tuple  Data Structure Result (Indexed List)
cursor = db.cursor (MySQLdb.cursors.DictCursor) # Dictonary Data Structure Result (Key Value List)
cursor.execute("SELECT `email`, `scores`,  `id` , `comment` FROM `team_name` ORDER BY id DESC ")
tdata = cursor.fetchall()
print(type(tdata)) # tuple type  data
print (tdata);
for row in tdata:
    print(type(row))   # dict type  data
    #print(row)
    #print('record  id===', int(row[0]), ' scores === ', row[1], ' email === ', row[2])
    print('record  id===', int(row['id']), ' scores === ', row['scores'], ' email === ', row['email'])
    #print(type(row['email'])) is similar to  print(type(row[2]))

# disconnect from server
db.close()
