import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from forms.des_setings_ip import *

from db import connect_db

class MyWin(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Выравнивание
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        
        self.row_count = 1
        
        # Подключение к бд
        self.records = connect_db("""SELECT INET_NTOA(ip), Location, Yi, Gor FROM ips""", 'all')
        
        # Цикл который заполняет данными таблицу
        for row in self.records:
            # -------------------------- добавление цветных кнопок
            self.clear_button = QPushButton("Удалить", self)
            self.clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.clear_button.setStyleSheet("QPushButton {\n"
        "    background-color: #fa7f72;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: white;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    color: #626AB0;\n"
        "    background-color: #D5D4D4;\n"
        "}")

            self.edit_button = QPushButton("Изменить", self)
            self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.edit_button.setStyleSheet("QPushButton {\n"
        "    background-color: #00b8ef;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: white;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    color: #626AB0;\n"
        "    background-color: #D5D4D4;\n"
        "}")
            # ---------------------------

            self.clear_button.clicked.connect(self.clear_item)
            self.clear_button.setToolTip("Удалить эту строку")
            self.edit_button.clicked.connect(self.edit_item)
            self.edit_button.setToolTip("Изменить эту строку -\n введите новые данные в\n нужные ячейки данной строки")

            table_index = self.tableWidget.rowCount()
            self.tableWidget.insertRow(table_index)

            self.tableWidget.setCellWidget(table_index, 0, self.clear_button)
            self.tableWidget.setCellWidget(table_index, 1, self.edit_button)
            self.tableWidget.setItem(table_index, 2, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(table_index, 3, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(table_index, 4, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(table_index, 5, QtWidgets.QTableWidgetItem(str(row[3])))

            table_index += 1
            self.row_count += 1

    @QtCore.pyqtSlot()
    def clear_item(self):
        button = self.sender()
        if button:
            result = QtWidgets.QMessageBox.question(self, "Внимение", "Удалить строку ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.No:
            QMessageBox.information(self, 'Внимание', 'Удаление отменено.')

        if result == QtWidgets.QMessageBox.Yes:
            row = self.tableWidget.indexAt(button.pos()).row()

            cols = self.tableWidget.columnCount()
            data = []
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget.item(row,col).text())
                except:
                    tmp.append('No data')
            data.append(tmp[2])

            for i in data:
                connect_db("DELETE FROM ips WHERE INET_NTOA(ip) = '{0}'".format(i), 'commit')

                self.tableWidget.removeRow(row)

                QMessageBox.information(self, "Внимание", "Строка удалена!")
    
    @QtCore.pyqtSlot()
    def edit_item(self):
        button = self.sender()
        if button:
            result = QtWidgets.QMessageBox.question(self, "Внимение", "Изменить строку ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.No:
            QMessageBox.information(self, 'Внимание', 'Изменение отменено.')

        if result == QtWidgets.QMessageBox.Yes:
            row = self.tableWidget.indexAt(button.pos()).row()

            cols = self.tableWidget.columnCount()
            data = []
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget.item(row,col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)

            for i in data:
                recor = connect_db("""SELECT id FROM ips WHERE ip = INET_ATON('{0}')""".format(i[2]), 'one')
                connect_db("""UPDATE ips SET ip = INET_ATON('{0}'), Location = '{1}', Yi = '{2}', Gor = '{3}' WHERE id = '{4}'""".format(i[2], i[3], i[4], i[5], recor[0], 'commit'))

                QMessageBox.information(self, "Внимание", "Строка изменена!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.resize(450, 200)
    w.show()
    sys.exit(app.exec_())