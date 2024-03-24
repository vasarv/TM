from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogTaskWindow,
    dialogFormFinance,
    dialogFinanceWindow,
)


def FinanceRmRecord():
    _translate = QtCore.QCoreApplication.translate
    dialogFormFinance.CaptionLabel.setText(
        _translate("DialogFormFinance", "Удаление записи финансов")
    )
    dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
    dialogFinanceWindow.show()
