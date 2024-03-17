import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM task')
users = cursor.fetchall()

# Выводим результаты
for user in users:
  print(user)
  
# Закрываем соединение
connection.close()

def add_values_to_table():
    rowPosition = tableWidget.rowCount() # смотрим сколько строк уже в таблице GUI
    tableWidget.insertRow(rowPosition) # перемещаемся к последней строке таблицы GUI

    for dat in user: # берем данные построчно из таблицы finance
        for colume in range(1, len(dat)): # перебираем колонки и добавляем в таблицы GUI
            tableWidget.setItem(
                rowPosition,
                colume - 1,
                QTableWidgetItem(str(dat[colume]))
            ) # добавляем данные столбец-в-столбец
        rowPosition += 1 # перемещаемся на строку вниз
