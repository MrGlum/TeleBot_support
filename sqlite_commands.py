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
    conn.close


def obnovit_staroe(userochek):
    try:
        cur.execute('UPDATE users VALUES(?,?,?,?)', userochek)
    except:
        return ("Что-то пошло не так!")
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
    conn.close


def zabrat_sql(intro):
    try:
        cur.execute(f"SELECT {intro} FROM users;")
        one_result = cur.fetchone()
        print(one_result)
    except:
        print('Нет такого в таблице!')
    conn.commit()
    conn.close

if __name__ == '__main__':
   sql = dobavit_novoe(['2', 'Hit', 'Laggers', 'male'])
   zabrat_sql('1')

