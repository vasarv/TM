from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)

from TaskAddRecord import status_dict
from DBfuncs import delete_as_DB, read_as_DB

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
                         WHERE today = {date}
                         """)

    delete_as_DB(f"""
                DELETE FROM task
                WHERE descript = {description} AND dates_id = {date_id} AND status = {status}
    """)

    dialogTaskWindow.close()