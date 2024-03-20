from formcreator import mainForm
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLineEdit
import sqlite3
import time
import datetime
from math import sqrt

def DBgetFinance(income: bool, dates: list[str, str]) -> list[list, float]:
    StrToDate = datetime.datetime.strptime
    dates = [StrToDate(date, '%d.%m.%Y').date() for date in dates]
    OutData = []
    Sum = 0

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
    data = cursor.fetchall()
    db.close()

    for dat in data:
        date = dat[1]
        print(dat)
        if dates[0] <= StrToDate(date, '%d.%m.%Y').date() <= dates[1]:
            OutData.append(OutData)
            Sum += int(dat[5])
        else:
            continue

    return [OutData, sqrt(Sum)]

def FinanceTableUpdate(data: list[tuple], income: bool = True):
    """
    Args:
        data (list): [id записи, date, статья расхода, count, sum]
    """

    # lineEditSumUpdate(total_amount=100.0, currency="RUB") # функция в разработке

    income: bool  # если фильтруем по доходам - True, по расходам - False
    tableWidget = mainForm.tableWidgetFinance
    data = [list(i) for i in GetDataTest()]

    if mainForm.radioButtonComing.isChecked():
        income = True
    elif mainForm.radioButtonExpenditure.isChecked():
        income = False

    rowPosition = tableWidget.rowCount()  # смотрим сколько строк уже в таблице GUI
    tableWidget.insertRow(rowPosition)  # перемещаемся к последней строке таблицы GUI

    for dat in data:  # берем данные построчно из таблицы finance
        for colume in range(
            1, len(dat)
        ):  # перебираем колонки и добавляем в таблицы GUI
            tableWidget.setItem(
                rowPosition, colume - 1, QTableWidgetItem(str(dat[colume]))
            )  # добавляем данные столбец-в-столбец
        rowPosition += 1  # перемещаемся на строку вниз


def lineEditSumUpdate(total_amount: float = 0.0, currency: str = "рублей"): #пофиксить функцию
    LineEdit = mainForm.lineEditSum
    LineEdit.setEnabled(True)
    # LineEdit.setReadOnly(True)
    LineEdit.setText(f"{total_amount} {currency}") 
