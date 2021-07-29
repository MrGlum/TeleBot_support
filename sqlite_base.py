import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

conn.commit()

def dobavit_novoe(userochek):
   try:
      cur.execute('INSERT INTO users VALUES(?,?,?,?)', userochek)
   except:
      return ("Запись с таким номером есть!")
   conn.commit()

conn.commit()
conn.close

def obnovit_staroe(userochek):
   try:
      cur.execute('UPDATE users VALUES(?,?,?,?)', userochek)
   except:
      return ("Что-то пошло не так!")
   conn.commit()

conn.commit()
conn.close

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

def zabrat_sql():
   try:
      pass
   except:
      pass

sql = dobavit_novoe(['2','Hit', 'Laggers', 'male'])
