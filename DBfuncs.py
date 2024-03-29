import sqlite3


def insert_to_DB(request: str, db_name: str = "tasks.db") -> int:
    InsertID = -1

    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute(request)
        InsertID = cursor.lastrowid
    except sqlite3.OperationalError as e:
        print("Syntax error: ", e)
    finally:
        connection.commit()
        connection.close()

    return InsertID


def read_as_DB(request: str, db_name: str = "tasks.db") -> list:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute(request)

    data = cursor.fetchall()

    connection.close()

    return [list(data) for dat in data]

def delete_as_DB(request: str, db_name: str = "tasks.db"):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute(request)
    finally:
        connection.commit()
        connection.close()