import sqlite3
conn = sqlite3.connect('database.test')
c = conn.cursor()
create_table_query = '''CREATE TABLE user ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, code TEXT NOT NULL);'''
insert_table_query = ''' INSERT INTO user values (10, 'selenium', '454545');'''
read_table_query = '''SELECT * FROM user;'''

#c.execute(create_table_query)
#c.execute(insert_table_query)
c.execute(read_table_query)

conn.commit()

data = c.fetchall()

usernanme = []
password = []

for row in data:
    usernanme.append(row[1])
    password.append(row[2])

print(usernanme)
print(password)