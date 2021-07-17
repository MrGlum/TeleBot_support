import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

conn.commit()

def dobavit_novoe(userochek):
   try:
      cur.execute('INSERT INTO users VALUES(?,?,?,?)', userochek)
   except:
      print("NOOOOOOO!")
   conn.commit()

conn.commit()

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
