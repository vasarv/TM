from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)
from DBfuncs import insert_to_DB
from DialogFormFinance.FinanceAddRecord import FinanceAddRecordWindow
from DialogFormFinance.FinanceRmRecord import FinanceRmRecord
from DialogFormFinance.FinanceEditRecord import FinanceEditRecord
from DialogFormTask.TaskAddRecord import TaskAddRecordWindow
from DialogFormTask.TaskRmRecord import TaskRmRecord
from DialogFormTask.TaskEditRecord import TaskEditRecord



def AddRecordClick():
    if mainForm.tabWidget.currentIndex() == 0:
<<<<<<< HEAD
        TaskAddRecordWindow()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceAddRecordWindow()
=======
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Добавление записи"))
        dialogFormTask.dateEditTask.setDate(QDate.currentDate())
        dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
        dialogTaskWindow.show()
    else:
        pass
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219

def DelRecordClick():
    if mainForm.tabWidget.currentIndex() == 0:
<<<<<<< HEAD
        TaskRmRecord()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceRmRecord()

=======
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Удаление записи"))
        dialogTaskWindow.show()
    else:
        pass
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219

def EditRecordClick():
    if mainForm.tabWidget.currentIndex() == 0:
<<<<<<< HEAD
        TaskEditRecord()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceEditRecord()
=======
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Изменение записи"))
        dialogTaskWindow.show()
    else:
        pass
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219
