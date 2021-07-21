import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

more_users = [('00006', 'Peter', 'Parker', 'Male'), ('00007', 'Bruce', 'Wayne', 'male')]
#cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)

conn.commit()
conn.close

conn.execute("DELETE users")
