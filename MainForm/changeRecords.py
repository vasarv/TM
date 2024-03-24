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
        TaskAddRecordWindow()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceAddRecordWindow()

def DelRecordClick():
    if mainForm.tabWidget.currentIndex() == 0:
        TaskRmRecord()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceRmRecord()


def EditRecordClick():
    if mainForm.tabWidget.currentIndex() == 0:
        TaskEditRecord()
    elif mainForm.tabWidget.currentIndex() == 1:
        FinanceEditRecord()
