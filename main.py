from Flags import Flags

from formcreator import mainForm, dialogFormTask, app

from MainForm.onClickCalerdar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from MainForm.DatePeriod import SetDateIn, SetDateOut
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose

from MainForm.TabWidgetFuncs import FinanceTableUpdate, TasksTableUpdate


flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)

mainForm.radioButtonComing.clicked.connect(FinanceTableUpdate)
mainForm.radioButtonExpenditure.clicked.connect(FinanceTableUpdate)

TasksTableUpdate()
FinanceTableUpdate()

app.exec()
