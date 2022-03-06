from db_conn import cursor, db

cursor.execute("SELECT `email`, `scores`,  `id`  FROM `team_name` ORDER BY id DESC ")
db_data = cursor.fetchall()
print(type(db_data))  # tuple type  data
print(db_data)
for row in db_data:
    print(type(row))  # dict type  data
    # print(row)
    # print('record  id===', int(row[0]), ' scores === ', row[1], ' email === ', row[2])
    print('record  id===', int(row['id']), ' scores === ', row['scores'], ' email === ', row['email'])
    # print(type(row['email'])) is similar to  print(type(row[2]))

# disconnect from server
db.close()
