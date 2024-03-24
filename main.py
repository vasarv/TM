from formcreator import (
    mainForm,
    dialogFormTask,
    dialogFormFinance,
    app,
    dialogFinanceWindow,
    dialogTaskWindow,
)

from Flags import Flags

from MainForm.onClickCalerdar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from MainForm.DatePeriod import SetDateIn, SetDateOut

from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick

from DialogFormFinance.DialogFormFinanceClose import dialogFormFinanceClose
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose
from DialogFormTask.TaskAddRecord import TaskAddRecord
from DialogFormFinance.FinanceAddRecord import FinanceAddRecord

# from MainForm.changeRecords_Finance import AddRecordClick_Finance, DelRecordClick_Finance, EditRecordClick_Finance


flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

################
dialogFormTask.ButtonSave.clicked.connect(TaskAddRecord)
dialogFormFinance.ButtonSave.clicked.connect(FinanceAddRecord)

# TaskAddRecordWindow()
################

dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)
dialogFormFinance.ButtonCancel.clicked.connect(dialogFormFinanceClose)


app.exec()
