from formcreator import mainForm
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView

import sqlite3
import datetime
from math import sqrt


def lineEditSumUpdate(total_amount: float = 0.0, currency: str = "руб."):
    LineEdit = mainForm.lineEditSum
    LineEdit.setEnabled(False)
    LineEdit.setText(f"{total_amount} {currency}")


def FinanceTableUpdate():
    """
    Args:
        data (list): [id записи, date, статья расхода, count, sum]
    """

    tableWidget = mainForm.tableWidgetFinance
    StrToDate = datetime.datetime.strptime
    income: bool = mainForm.radioButtonComing.isChecked()  # если фильтруем по доходам - True, по расходам - False
    Sum = 0

    #############################################

    db = sqlite3.connect("tasks.db")
    cursor = db.cursor()

    if income:
        request = """SELECT finance.id, dates.today, income_types.descript, expance_types.descript, finance.amount, finance.price FROM finance
                    JOIN dates ON dates.id = finance.dates_id
                    JOIN income_types ON income_types.id = finance.inc_types_id 
                    JOIN expance_types ON expance_types.id = finance.exp_types_id
                    WHERE finance.inc_types_id NOT NULL
                """
    else:
        request = """SELECT finance.id, dates.today, income_types.descript, expance_types.descript, finance.amount, finance.price FROM finance
                    JOIN dates ON dates.id = finance.dates_id
                    JOIN income_types ON income_types.id = finance.inc_types_id 
                    JOIN expance_types ON expance_types.id = finance.exp_types_id
                    WHERE finance.exp_types_id NOT NULL
            """

    cursor.execute(request)
    data = [list(i) for i in cursor.fetchall()]
    db.close()

    if mainForm.checkBoxFilterDate.isChecked():
        date_finance = [
            mainForm.dateEditIn.dateTime().toString("dd.MM.yyyy"),
            mainForm.dateEditOut.dateTime().toString("dd.MM.yyyy"),
        ]
    else:
        date_finance = [
            mainForm.calendarWidget.selectedDate().toString("dd.MM.yyyy")
            for _ in range(2)
        ]

    date_finance = [StrToDate(date, "%d.%m.%Y").date() for date in date_finance]

    #############################################

    tableWidget.setRowCount(0)  # очищаем таблицу
    tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # ставим запрет на изменение данных

    rowPosition = tableWidget.rowCount()  # смотрим сколько строк уже в таблице GUI
    tableWidget.insertRow(rowPosition)  # перемещаемся к последней строке таблицы GUI

    for dat in data:  # берем данные построчно из таблицы finance
        if (date_finance[0] <= StrToDate(str(dat[0]), "%d.%m.%Y").date() <= date_finance[1]):
            for idx in range(0, len(dat)):  # перебираем колонки и добавляем в таблицы GUI
                tableWidget.setItem(rowPosition, idx, QTableWidgetItem(str(dat[idx])))  # добавляем данные столбец-в-столбец
                Sum += int(dat[4]) * int(dat[5]) # Добавляем в сумму цену
            rowPosition += 1  # перемещаемся на строку вниз
        else:
            continue

    lineEditSumUpdate(Sum)
