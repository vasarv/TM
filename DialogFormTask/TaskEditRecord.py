from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)


def TaskEditRecord():
    _translate = QtCore.QCoreApplication.translate
    dialogFormTask.CaptionLabel.setText(
        _translate("DialogFormTask", "Изменение записи заданий")
    )
    dialogTaskWindow.show()