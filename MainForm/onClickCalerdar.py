from formcreator import mainForm
from MainForm.TabWidgetFuncs import TasksTableUpdate
from MainForm.TabWidgetFuncs import FinanceTableUpdate, TasksTableUpdate

def onClickCalendar():
    FinanceTableUpdate()
    TasksTableUpdate()