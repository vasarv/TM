from formcreator import mainForm, dialogFormTask, app

from Flags import Flags

from MainForm.onClickCalerdar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from MainForm.DatePeriod import SetDateIn, SetDateOut
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose
from MainForm.TasksUpdate import TasksTableUpdate







flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

mainForm.tabWidget.currentChanged.connect(TasksTableUpdate)

dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)




app.exec()