#!/usr/bin/env python3

import subprocess
import sys
from datetime import datetime

import authorization
from add_label import MyWin as Window_2
from forms.des import *
from setings_ip import MyWin as Window_3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import socket

from db import connect_db

class CheckEthernet:
    @staticmethod
    def ethernet():
        try:
            socket.gethostbyaddr('www.yandex.ru')
        except socket.gaierror:
            return False
        return True

class AuthWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth = authorization.Ui_Form()
        self.auth.setupUi(self)
        self.setWindowModality(2)
        self.validate_flag = False
        self.auth.lineEdit.setPlaceholderText('Password..')
        self.auth.pushButton.clicked.connect(self.check_passw)

    def check_passw(self):
        text = self.auth.lineEdit.text()
        if text:
            reader = connect_db("SELECT * FROM password", 'one')
            if text == reader[0]:
                self.validate_flag = True
                self.close()
                QMessageBox.information(self, '', 'Добро пожаловать!')
            else:
                QMessageBox.information(self, 'Внимание', 'Пароль введён неверно!')
        else:
            QMessageBox.information(self, 'Внимание', 'Введите пароль!')

    def closeEvent(self, value):
        if not self.validate_flag:
            raise SystemExit

class WorkThread(QtCore.QThread):
    threadSignal = QtCore.pyqtSignal(int, str, tuple)
        
    def __init__(self, dictIP):
        super().__init__()
        self.dictIP = dictIP

    def run(self):
        while True:
            for k, v in self.dictIP.items():
                if v[2] == 2:
                    response = subprocess.run(["ping", k, "-n", "1", "-w", "100"], shell=True, stdout=subprocess.PIPE).returncode
                    if not CheckEthernet.ethernet():
                        response = 1
                    self.msleep(1)
                    self.threadSignal.emit(response, k, v)

class WorkThread_1(QtCore.QThread):
    threadSignal_1 = QtCore.pyqtSignal(int, str, tuple)

    def __init__(self, k, v):
        super().__init__()
        self.k_1 = k
        self.v_1 = v

    def run(self):
        response_1 = subprocess.run(["ping", self.k_1, "-n", "4", "-w", "100"], shell=True, stdout=subprocess.PIPE).returncode
        if not CheckEthernet.ethernet():
            response_1 = 1
        self.msleep(1)
        self.threadSignal_1.emit(response_1, self.k_1, self.v_1)

class Label(QLabel):
    clicked = QtCore.pyqtSignal(str, str)

    def __init__(self, background=QColor("white"), parent=None):
        super().__init__(parent)
        self._background = background
        self._change_stylesheet()
        self.setFixedSize(10, 10)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        if self._background != color:
            self._background = color
            self._change_stylesheet()

    def _change_stylesheet(self):
        qss = f"""QLabel {{
                    background-color:{self.background.name()};
                    border-radius: 5px;
                    min-height: 10px;
                    max-height: 10px;
                    min-width: 10px;
                    max-width: 10px;
                    border-style: solid;
                    border-color: black;
                    border-width: 1px;
                }}"""
        self.setStyleSheet(qss)

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName(), self.text())
        self._set_border_color("white")

    def mouseReleaseEvent(self, event):
        self._set_border_color("black")

    def _set_border_color(self, color):
        qss = f"""QLabel {{
                    background-color:{self.background.name()};
                    border-radius: 5px;
                    min-height: 10px;
                    max-height: 10px;
                    min-width: 10px;
                    max-width: 10px;
                    border-style: solid;
                    border-color: {color};
                    border-width: 1px;
                }}"""
        self.setStyleSheet(qss)

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.thread = None
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.ui.plainTextEdit.setReadOnly(True)
        self.table_index = 0
        self.row_count = 1
        self.count = 0
        self.dictMove = {}
        self.tab()
        self.thread_1_list = []
        self.thread_1_num = 0
        self.dictLbls = {}

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(self.startThread)
        self.ui.pushButton_2.clicked.connect(self.clear_plainText)
        self.ui.pushButton_3.clicked.connect(self.setings_ip_window)
        self.ui.pushButton_5.clicked.connect(self.add_label)
        self.ui.pushButton_6.clicked.connect(self.update_table)

    def add_label(self):
        if self.thread:
            self.startThread()
        self.window_2 = Window_2()
        self.window_2.setWindowModality(2)
        self.window_2.show()

    def coordinate(self, response, iP):
        _lbl = self.dictLbls.get(iP)
        if not _lbl:
            lab = Label(parent=self.ui.tab)
            lab.clicked.connect(self.onClickLabel)
            lab.setObjectName(f"  {iP}")
            records = connect_db(f"SELECT Yi, Gor, Location FROM ips WHERE INET_NTOA(ip) = '{iP}'", 'all')
            for Yi, Gor, Location in records:
                lab.setText(f"   {Yi},   {Gor},   {Location}")
            lab.move(*self.dictMove[iP])
            self.dictLbls[iP] = lab
        else:
            lab = _lbl
            lab.background = QColor("#fa7f72" if response == 1 else "#ffaa00" if iP else "#54e346")
            lab.show()

    def onClickLabel(self, objName, text):
        self.ui.statusbar.showMessage(f'Вы кликнули: {objName}, {text}')

    def tab(self):
        records = connect_db("SELECT INET_NTOA(ip), Yi, x, y FROM ips", 'all')
        self.dictMove = {ip: (x, y) for ip, yi, x, y in records}
        for row, value in enumerate(records):
            self.ui.tableWidget.setRowCount(self.row_count)
            item = QtWidgets.QTableWidgetItem(str(value[0]))
            item_2 = QtWidgets.QTableWidgetItem(str(value[1]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.ui.tableWidget.setItem(row, 0, item)
            self.ui.tableWidget.setItem(row, 1, item_2)
            self.row_count += 1

    def clear_plainText(self):
        self.ui.plainTextEdit.clear()

    def startThread(self):
        dictIP = {}
        [lbl.hide() for lbl in self.dictLbls.values()]
        self.dictLbls = {}
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            item_2 = self.ui.tableWidget.item(row, 1)
            if item.checkState():
                item.setBackground(QtGui.QColor("white"))
                item_2.setBackground(QtGui.QColor("white"))
            else:
                item.setBackground(QtGui.QColor("#b2b2b2"))
                item_2.setBackground(QtGui.QColor("#b2b2b2"))
            dictIP[item.text()] = (row, 0, item.checkState())
        if self.thread is None:
            self.thread = WorkThread(dictIP)
            self.thread.threadSignal.connect(self.on_threadSignal)
            self.thread.threadSignal.connect(self.coordinate)
            self.thread.start()
            self.ui.pushButton.setText("Стоп")
            self.ui.pushButton.setStyleSheet(self.get_button_style("#fa7f72"))
        else:
            self.thread.terminate()
            self.thread = None
            self.ui.pushButton.setText("Старт")
            self.ui.pushButton.setStyleSheet(self.get_button_style("#54e346"))

    def get_button_style(self, color):
        return f"""QPushButton {{
                     background-color: {color};
                 }}
                 QPushButton:hover {{
                     background-color: white;
                 }}
                 QPushButton:pressed {{
                     color: #626AB0;
                     background-color: #D5D4D4;
                 }}"""

    def on_threadSignal(self, response, k, v):
        item = self.ui.tableWidget.item(v[0], v[1])
        item_2 = self.ui.tableWidget.item(v[0], v[1] + 1)
        if response == 1:
            thread_1 = WorkThread_1(k, v)
            self.thread_1_list.append(thread_1)
            self.thread_1_list[self.thread_1_num].threadSignal_1.connect(self.on_threadSignal_1)
            self.thread_1_list[self.thread_1_num].threadSignal_1.connect(self.coordinate)
            self.thread_1_list[self.thread_1_num].start()
            self.thread_1_num += 1
        else:
            item.setBackground(QtGui.QColor("#54e346"))
            item_2.setBackground(QtGui.QColor("#54e346"))

    def on_threadSignal_1(self, response_1, k_1, v_1):
        item_1 = self.ui.tableWidget.item(v_1[0], v_1[1])
        item_2 = self.ui.tableWidget.item(v_1[0], v_1[1] + 1)
        current_time = datetime.now().strftime("%H:%M:%S")
        if response_1:
            item_1.setBackground(QtGui.QColor("#fa7f72"))
            item_2.setBackground(QtGui.QColor("#fa7f72"))
            records = connect_db(f"SELECT * FROM ips WHERE INET_NTOA(ip) = '{k_1}'", 'all')
            for row in records:
                self.ui.plainTextEdit.appendPlainText(f'Время {current_time} \n{k_1} | {row[1]} | {row[2]}\n{row[3]}\n')
        else:
            item_1.setBackground(QtGui.QColor("#ffaa00"))
            item_2.setBackground(QtGui.QColor("#ffaa00"))

    def update_table(self):
        records = connect_db("SELECT INET_NTOA(ip) FROM ips", 'all')
        table_index = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(table_index)
        if len(records) == table_index:
            self.ui.tableWidget.clearContents()
            self.tab()
            self.ui.tableWidget.setRowCount(table_index)
        elif len(records) > table_index:
            con = len(records) - table_index
            self.ui.tableWidget.clearContents()
            self.tab()
            self.ui.tableWidget.setRowCount(table_index + con)
        elif len(records) < table_index:
            con = table_index - len(records)
            self.ui.tableWidget.clearContents()
            self.tab()
            self.ui.tableWidget.setRowCount(table_index - con)

    def setings_ip_window(self):
        if self.thread:
            self.startThread()
        self.window_3 = Window_3()
        self.window_3.setWindowModality(2)
        self.window_3.show()

    def closeEvent(self, value):
        result = QtWidgets.QMessageBox.question(self, "Оповещание", "Закрыть программу ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.No:
            value.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    auth = AuthWindow()
    myapp.show()
    if not CheckEthernet.ethernet():
        QMessageBox.information(myapp, 'Внимание', 'Нет подключения к интернету!')
    auth.show()
    sys.exit(app.exec_())