from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import (
    dialogFormFinance,
    dialogFinanceWindow
)

from DBfuncs import insert_to_DB, read_as_DB

types_dict: dict = {
    "Доход": "income",
    "Расход": "expance"
}

def FinanceAddRecordWindow():
    _translate = QtCore.QCoreApplication.translate

    dialogFormFinance.CaptionLabel.setText(
        _translate("DialogFormFinance", "Добавление записи финансов")
    )
    dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
    dialogFinanceWindow.show()

    # dialogFinanceWindow.dateEditFinance.setEnabled(False)

def FinanceAddRecord():
    date = dialogFormFinance.dateEditFinance.dateTime().toString('dd.MM.yyyy')
    article_type = str(types_dict[dialogFormFinance.comboBoxArticleType.currentText()])
    article_text = str(dialogFormFinance.textEditArticle.toPlainText()).lower()
    amount = dialogFormFinance.textEditCount.toPlainText()
    price = dialogFormFinance.textEditSum.toPlainText()
    
    if not(price.replace('.','',1).isdigit()):
        return #PRINT ERROR
    elif not(amount.isdigit()):
        return #PRINT ERROR

    insert_to_DB(f"""
                INSERT INTO {article_type}_types (descript)
                SELECT DISTINCT '{article_text}'
                FROM {article_type}_types
                WHERE '{article_text}' NOT IN (SELECT descript FROM {article_type}_types);
                """)

    date_id = insert_to_DB(f"""
                        INSERT INTO dates (today)
                        SELECT DISTINCT '{date}'
                        FROM dates
                        WHERE '{date}' NOT IN (SELECT today FROM dates);
                        """
    )

    article_id = read_as_DB(f"""SELECT id FROM {article_type}_types WHERE descript="{article_text}";""")
    article_id = str(*article_id[0][0])
    
    if article_type == "income":
        insert_to_DB(f"""
                    INSERT INTO finance (dates_id, inc_types_id, exp_types_id, amount, price)
                    VALUES ({date_id}, {article_id}, -1, {amount}, {price});
                    """)
    elif article_type == "expance":
        insert_to_DB(f"""
                    INSERT INTO finance (dates_id, inc_types_id, exp_types_id, amount, price)
                    VALUES ({date_id}, -1, {article_id}, {amount}, {price});
                    """)

    dialogFinanceWindow.close()