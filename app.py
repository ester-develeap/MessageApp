from config import DATABASE
from src.api import app
from src.message_db import message_db

if __name__ == '__main__':
    conn = message_db.create_connection(DATABASE)
    if conn is not None:
        message_db.init_db(conn)
    else:
        print("Error! cannot create the database connection.")
        exit(1)

    app.run()




