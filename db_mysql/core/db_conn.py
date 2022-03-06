import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "password", "dev_data")

# prepare a cursor object using cursor() method
# tuple  Data Structure Result (Indexed List)
# cursor = db.cursor()
# dictionary Data Structure Result (Key Value List)
cursor = db.cursor(MySQLdb.cursors.DictCursor)
