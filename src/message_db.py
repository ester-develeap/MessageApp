import sqlite3
from sqlite3 import Error

class message_db:

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def init_db(conn):
        sql_create_message_table = """
                            CREATE TABLE IF NOT EXISTS message(
                            application_id INTEGER NOT NULL,
                            session_id TEXT NOT NULL,
                            message_id TEXT PRIMARY KEY,
                            participants TEXT NOT NULL,
                            content TEXT DEFAULT "" 
                            );
                            """
        message_db.create_table(conn, sql_create_message_table)

    @staticmethod
    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    @staticmethod
    def insert_message(conn, message):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO message(application_id,session_id,message_id,participants,content)
                      VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, message)
        return cur.lastrowid

    @staticmethod
    def update_message(conn, message):
        """
        update priority, begin_date, and end date of a task
        :param conn:
        :param task:
        :return: project id
        """
        sql = ''' UPDATE message
                  SET application_id = ? ,
                      session_id = ? ,
                      participants= ? ,
                      content= ?
                  WHERE message_id = ?'''
        cur = conn.cursor()
        cur.execute(sql, message)
        conn.commit()

    @staticmethod
    def delete_message(conn,id,value):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        if id == 'application_id':
            sql = 'DELETE FROM message WHERE application_id=?'
        elif id == 'session_id':
            sql = 'DELETE FROM message WHERE session_id=?'
        elif id == 'message_id':
            sql = 'DELETE FROM message WHERE message_id=?'
        else:
            return
        cur = conn.cursor()
        cur.execute(sql, (value,))
        conn.commit()

    @staticmethod
    def select_all_messages(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM message")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    @staticmethod
    def select_specific_messages(conn,id,value):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        if id == 'application_id':
            sql = 'SELECT * FROM message WHERE application_id=?'
        elif id == 'session_id':
            sql = 'SELECT * FROM message WHERE session_id=?'
        elif id == 'message_id':
            sql = 'SELECT * FROM message WHERE message_id=?'
        else:
            return
        cur = conn.cursor()
        cur.execute(sql, (value,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
