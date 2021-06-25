from getpass import getpass
from logging import root
from mysql.connector import connect, Error

import config

try:
    with connect(
        host="localhost",
        user= config.name,
        password= config.pasSQL,
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)