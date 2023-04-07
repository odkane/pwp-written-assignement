import sqlite3
from sqlite3 import Connection, Error


def create_connection(db_file) -> Connection:
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



def create_table(conn: Connection, create_table_sql: str):
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


def create_table_sql(table_name: str, no_columns: int) -> str:
    columns = ['y{} FLOAT'.format(i+1) for i in range(no_columns)] if no_columns > 1 else ['y FLOAT']
    
    return """ CREATE TABLE IF NOT EXISTS {} (
            x float PRIMARY KEY,
            {}
            ); """.format(table_name, ', '.join(columns))


def create_tables(db_name: str):
    database = rf'{db_name}'

    test_table_sql = create_table_sql("test", 1)
    train_table_sql = create_table_sql("train", 4)
    ideal_table_sql = create_table_sql("ideal", 50)
    print(train_table_sql)
    print(test_table_sql)

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create test table
        create_table(conn, test_table_sql)
        
        # create train table
        create_table(conn, train_table_sql)

        # create ideal table
        create_table(conn, ideal_table_sql)
    else:
        print("Error! cannot create the database connection.")

