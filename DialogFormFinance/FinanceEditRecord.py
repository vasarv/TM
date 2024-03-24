from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)


def FinanceEditRecord():
    _translate = QtCore.QCoreApplication.translate
    dialogFormFinance.CaptionLabel.setText(
        _translate("DialogFormFinance", "Изменение финансов")
    )
    dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
    dialogFinanceWindow.show()
