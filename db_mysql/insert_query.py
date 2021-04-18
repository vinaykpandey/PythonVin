from db_conn import cursor, db

sql = "INSERT INTO `team_name`  SET `scores` = '40' , `email` = 'abc1@gmail.com' "
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except Exception as e:
    print(e)
    # Rollback in
    db.rollback()

# disconnect from server
db.close()
