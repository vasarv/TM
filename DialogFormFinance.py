# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kostya\Documents\Python Scripts\TM-main\DialogFormFinance.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogFormFinance(object):
    def setupUi(self, DialogFormFinance):
        DialogFormFinance.setObjectName("DialogFormFinance")
        DialogFormFinance.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogFormFinance.resize(400, 300)
        DialogFormFinance.setMaximumSize(QtCore.QSize(400, 300))
        DialogFormFinance.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CaptionLabel = QtWidgets.QLabel(DialogFormFinance)
        self.CaptionLabel.setGeometry(QtCore.QRect(80, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.label_2 = QtWidgets.QLabel(DialogFormFinance)
        self.label_2.setGeometry(QtCore.QRect(10, 34, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogFormFinance)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(DialogFormFinance)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateEditFinance = QtWidgets.QDateEdit(DialogFormFinance)
        self.dateEditFinance.setGeometry(QtCore.QRect(130, 34, 241, 22))
        self.dateEditFinance.setCalendarPopup(True)
        self.dateEditFinance.setObjectName("dateEditFinance")
        self.textEditFinance = QtWidgets.QTextEdit(DialogFormFinance)
        self.textEditFinance.setGeometry(QtCore.QRect(130, 59, 241, 21))
        self.textEditFinance.setObjectName("textEditFinance")
        self.ButtonSave = QtWidgets.QPushButton(DialogFormFinance)
        self.ButtonSave.setGeometry(QtCore.QRect(180, 260, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonSave.setFont(font)
        self.ButtonSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\kostya\\Documents\\Python Scripts\\TM-main\\icons/save48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSave.setIcon(icon)
        self.ButtonSave.setFlat(True)
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonCancel = QtWidgets.QPushButton(DialogFormFinance)
        self.ButtonCancel.setGeometry(QtCore.QRect(284, 260, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonCancel.setFont(font)
        self.ButtonCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\kostya\\Documents\\Python Scripts\\TM-main\\icons/delete48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonCancel.setIcon(icon1)
        self.ButtonCancel.setFlat(True)
        self.ButtonCancel.setObjectName("ButtonCancel")
        self.label_6 = QtWidgets.QLabel(DialogFormFinance)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEditFinance_2 = QtWidgets.QTextEdit(DialogFormFinance)
        self.textEditFinance_2.setGeometry(QtCore.QRect(130, 100, 241, 21))
        self.textEditFinance_2.setObjectName("textEditFinance_2")
        self.textEditFinance_3 = QtWidgets.QTextEdit(DialogFormFinance)
        self.textEditFinance_3.setGeometry(QtCore.QRect(130, 140, 241, 21))
        self.textEditFinance_3.setObjectName("textEditFinance_3")
        self.label_7 = QtWidgets.QLabel(DialogFormFinance)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEditFinance_4 = QtWidgets.QTextEdit(DialogFormFinance)
        self.textEditFinance_4.setGeometry(QtCore.QRect(130, 180, 241, 21))
        self.textEditFinance_4.setObjectName("textEditFinance_4")

        self.retranslateUi(DialogFormFinance)
        QtCore.QMetaObject.connectSlotsByName(DialogFormFinance)

    def retranslateUi(self, DialogFormFinance):
        _translate = QtCore.QCoreApplication.translate
        DialogFormFinance.setWindowTitle(_translate("DialogFormFinance", "Работа с записями"))
        self.CaptionLabel.setText(_translate("DialogFormFinance", "Добавление записи в базу"))
        self.label_2.setText(_translate("DialogFormFinance", "Дата"))
        self.label_3.setText(_translate("DialogFormFinance", "Статья дохода"))
        self.label_5.setText(_translate("DialogFormFinance", "Количество"))
        self.ButtonSave.setText(_translate("DialogFormFinance", "Сохранить"))
        self.ButtonCancel.setText(_translate("DialogFormFinance", "Отменить"))
        self.label_6.setText(_translate("DialogFormFinance", "Статья расхода"))
        self.label_7.setText(_translate("DialogFormFinance", "Сумма"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogFormFinance = QtWidgets.QDialog()
    ui = Ui_DialogFormFinance()
    ui.setupUi(DialogFormFinance)
    DialogFormFinance.show()
    sys.exit(app.exec_())
