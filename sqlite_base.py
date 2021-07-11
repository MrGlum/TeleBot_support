import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

conn.commit()

try:
   cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
      VALUES('00001', 'Alex', 'Smith', 'male');""")
except:
   print("NOOOOOOO!")


conn.commit()

if __name__ == '__main__':
   try:
      cur.execute("""CREATE TABLE IF NOT EXISTS users(
      userid INT PRIMARY KEY,
      fname TEXT,
      lname TEXT,
      gender TEXT);
      """)
   except:
      print("I have this table!")