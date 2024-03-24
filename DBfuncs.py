import sqlite3

def insert_to_DB(request: str, db_name: str = "tasks.db") -> int:
    InsertID = -1

    try:
        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()

        cursor.execute(request)
        InsertID = connection.insert_id()
    except:
        pass
    finally:
        connection.commit()
        connection.close()
    
    return InsertID