from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)


def AddRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(
            _translate("DialogFormTask", "Добавление записи заданий")
        )
        dialogFormTask.dateEditTask.setDate(QDate.currentDate())
        dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
        dialogTaskWindow.show()

    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.CaptionLabel.setText(
            _translate("DialogFormFinance", "Добавление записи финансов")
        )
        dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
        dialogFinanceWindow.show()


def DelRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(
            _translate("DialogFormTask", "Удаление записи заданий")
        )
        dialogTaskWindow.show()
    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.CaptionLabel.setText(
            _translate("DialogFormFinance", "Удаление записи финансов")
        )
        dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
        dialogFinanceWindow.show()


def EditRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(
            _translate("DialogFormTask", "Изменение записи заданий")
        )
        dialogTaskWindow.show()
    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.CaptionLabel.setText(
            _translate("DialogFormFinance", "Изменение финансов")
        )
        dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
        dialogFinanceWindow.show()
