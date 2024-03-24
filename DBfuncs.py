import sqlite3

def insert_to_DB(request: str, db_name: str = "tasks.db") -> int:
    InsertID = -1

    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute(request)
        InsertID = connection.insert_id()
    except:
        pass
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

    return data
