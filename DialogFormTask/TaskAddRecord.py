from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    dialogFormTask,
    dialogTaskWindow
)

from DBfuncs import insert_to_DB

status_dict: dict = {
    "Получена": "received",
    "Начата": "started",
    "Завершена": "completed",
}


def TaskAddRecordWindow():
    _translate = QtCore.QCoreApplication.translate
    dialogFormTask.CaptionLabel.setText(
        _translate("DialogFormTask", "Добавление записи заданий")
    )
    dialogFormTask.dateEditTask.setDate(QDate.currentDate())
    dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
    dialogTaskWindow.show()

def TaskAddRecord():
    date = dialogFormTask.dateEditTask.dateTime().toString('dd.MM.yyyy')
    description = dialogFormTask.textEditTask.toPlainText()
    time_start = dialogFormTask.timeEditStart.time().toString('hh:mm')
    time_end = dialogFormTask.timeEditEnd.time().toString('hh:mm')
    status = status_dict[dialogFormTask.comboBoxTaskStatus.currentText()]

    date_id = insert_to_DB(f"""
                           INSERT INTO dates (today)
                           VALUES ("{date}")
                           """
    )

    insert_to_DB(f"""
                 INSERT INTO task (decript, time_start, time_end, dates_id, status)
                 VALUES ("{description}", "{time_start}", "{time_end}", {date_id}, "{status}");
                 """
    )
    
    dialogTaskWindow.close()
