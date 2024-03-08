from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

MainForm, Window = uic.loadUiType("MainForm.ui")
DialogFormTask, DialogTaskWindow = uic.loadUiType("DialogFormTask.ui")


app = QApplication([])
mainWindow = Window()
dialogTaskWindow = DialogTaskWindow()

mainForm = MainForm()
dialogFormTask = DialogFormTask()

mainForm.setupUi(mainWindow)
dialogFormTask.setupUi(dialogTaskWindow)


mainWindow.show()


