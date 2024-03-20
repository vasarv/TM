import sqlite3
from formcreator import mainForm
from PyQt5.QtWidgets import QTableWidgetItem
import datetime


def TasksTableUpdate():
    print("changed!")
    StrToDate = datetime.datetime.strptime
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("""
                   SELECT task.id, task.decript, task.time_start, task.time_end, dates.today, task.status FROM task
                   JOIN dates ON dates.id = task.dates_id
                   """)

    tasks = cursor.fetchall()
    connection.close()

    date_task: list[str, str] = ["01.07.2000", "01.05.2024"]
    date_task = [StrToDate(date, '%d.%m.%Y').date() for date in date_task]

    tableWidget = mainForm.tableWidgetTask
    rowPosition = tableWidget.rowCount()  # смотрим сколько строк уже в таблице GUI
    tableWidget.insertRow(rowPosition)  # перемещаемся к последней строке таблицы GUI
    
    for dat in [
        list(task) for task in tasks
    ]:  # берем данные построчно из таблицы finance
        if date_task[0] <= StrToDate(dat[4], '%d.%m.%Y').date() <= date_task[1]:
            for colume in range(
                1, len(dat)
            ):  # перебираем колонки и добавляем в таблицы GUI
                tableWidget.setItem(
                    rowPosition, colume - 1, QTableWidgetItem(str(dat[colume]))
                )  # добавляем данные столбец-в-столбец
            rowPosition += 1  # перемещаемся на строку вниз
