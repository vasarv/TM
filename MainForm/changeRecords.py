from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import mainForm, dialogFormTask, dialogTaskWindow

def AddRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Добавление записи"))
        dialogFormTask.dateEditTask.setDate(QDate.currentDate())
        dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
        dialogTaskWindow.show()

    else:
        pass

def DelRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Удаление записи"))
        dialogTaskWindow.show()
    
    else:
        pass

def EditRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Изменение записи"))
        dialogTaskWindow.show()
    
    else:
        pass