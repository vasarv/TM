<<<<<<< HEAD
from formcreator import (
    mainForm,
    dialogFormTask,
    dialogFormFinance,
    app,
    dialogFinanceWindow,
    dialogTaskWindow,
)

=======
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219
from Flags import Flags

from formcreator import mainForm, dialogFormTask, app

from MainForm.onClickCalerdar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from MainForm.DatePeriod import SetDateIn, SetDateOut

from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick

from DialogFormFinance.DialogFormFinanceClose import dialogFormFinanceClose
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose
from DialogFormTask.TaskAddRecord import TaskAddRecord
from DialogFormFinance.FinanceAddRecord import FinanceAddRecord

<<<<<<< HEAD
# from MainForm.changeRecords_Finance import AddRecordClick_Finance, DelRecordClick_Finance, EditRecordClick_Finance
=======
from MainForm.TabWidgetFuncs import FinanceTableUpdate, TasksTableUpdate
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219


flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)

<<<<<<< HEAD
################
dialogFormTask.ButtonSave.clicked.connect(TaskAddRecord)
dialogFormFinance.ButtonSave.clicked.connect(FinanceAddRecord)

# TaskAddRecordWindow()
################

=======
>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219
dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)
dialogFormFinance.ButtonCancel.clicked.connect(dialogFormFinanceClose)

mainForm.radioButtonComing.clicked.connect(FinanceTableUpdate)
mainForm.radioButtonExpenditure.clicked.connect(FinanceTableUpdate)

<<<<<<< HEAD
=======
TasksTableUpdate()
FinanceTableUpdate()

>>>>>>> 597ee6d37da1e541f93ba8b053ad87e710aa6219
app.exec()
