from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)

from DBfuncs import delete_as_DB, read_as_DB

status_dict: dict = {
    "Получена": "received",
    "Начата": "started",
    "Завершена": "completed",
}

def TaskRmRecordWindow():
    _translate = QtCore.QCoreApplication.translate
    dialogFormTask.CaptionLabel.setText(
        _translate("DialogFormTask", "Удаление записи заданий")
    )
    dialogTaskWindow.show()

def TaskRmRecord():
    date = dialogFormTask.dateEditTask.dateTime().toString('dd.MM.yyyy')
    description = dialogFormTask.textEditTask.toPlainText()
    time_start = dialogFormTask.timeEditStart.time().toString('hh:mm')
    time_end = dialogFormTask.timeEditEnd.time().toString('hh:mm')
    status = status_dict[dialogFormTask.comboBoxTaskStatus.currentText()]

    date_id = read_as_DB(f"""
                         SELECT id FROM dates
                         WHERE today = "{date}"
                         """)[0]
    
    print(date_id)

    delete_as_DB(f"""
                DELETE FROM task
                WHERE descript = "{description}" AND dates_id = {date_id} AND status = "{status}"
    """)

    dialogTaskWindow.close()