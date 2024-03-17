from formcreator import mainForm, dialogFormTask, app

from Flags import Flags

from MainForm.onClickCalerdar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from MainForm.DatePeriod import SetDateIn, SetDateOut
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from MainForm.FinanceTabUpdates import FinanceTableUpdate, lineEditSumUpdate
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose





flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

mainForm.radioButtonComing.clicked.connect(FinanceTableUpdate) #приход
# mainForm.radioButtonExpenditure.clicked.connect(SetTableWidgetItems) #расход


dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)




app.exec()