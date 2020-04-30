from src.api import app
from src.message_db import message_db

if __name__ == '__main__':
    app.run()

    # create a database connection
    #conn = message_db.create_connection(DATABASE)

    # create tables
    #if conn is not None:
        # create projects table
        #init_db(conn)
    # else:
    #     print("Error! cannot create the database connection.")

    # with conn:
    #     # create a new project
    #     message = (1, "wewe", "ddd", "['avi','moshe']", "wow");
    #     row_id = insert_message(conn, message)
    #     print(row_id)
    #     delete_message(conn,'application_id',1);
    #
    #     select_all_messages(conn)
    #     select_specific_messages(conn,'application_id',2)
