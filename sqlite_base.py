import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

conn.commit()

<<<<<<< HEAD
more_users = [('00006', 'Peter', 'Parker', 'Male'), ('00007', 'Bruce', 'Wayne', 'male')]
#cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
=======
def dobavit_novoe(userochek):
   try:
      cur.execute('INSERT INTO users VALUES(?,?,?,?)', userochek)
   except:
      print("NOOOOOOO!")
   conn.commit()
>>>>>>> 22e2db142cf4b4ad9cf84db4c542af78e32b3c71

conn.commit()
conn.close

<<<<<<< HEAD
conn.execute("DELETE users")
=======
def new_table_data():
   try:
      cur.execute("""CREATE TABLE IF NOT EXISTS users(
      userid INT PRIMARY KEY,
      fname TEXT,
      lname TEXT,
      gender TEXT);
      """)
   except:
      print("I have this table!")
   conn.commit()



print("Results from a LIKE query:")
sql = "SELECT * FROM users WHERE userid LIKE '12'"
print(cur.execute(sql).description)
>>>>>>> 22e2db142cf4b4ad9cf84db4c542af78e32b3c71
