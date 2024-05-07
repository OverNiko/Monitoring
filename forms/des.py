# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/Python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#00b8ef;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: #b2b2b2;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 691, 383))
        self.label_3.setStyleSheet("border-image: url(:/img/Снимок.PNG);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #54e346;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #626AB0;\n"
"    background-color: #D5D4D4;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setToolTip("")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 5, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton_3.setMaximumSize(QtCore.QSize(1369, 31))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #FFAA00;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #626AB0;\n"
"    background-color: #D5D4D4;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(133, 31))
        self.pushButton_6.setMaximumSize(QtCore.QSize(133, 31))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #FFAA00;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #626AB0;\n"
"    background-color: #D5D4D4;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setMinimumSize(QtCore.QSize(133, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(133, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #54e346;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #626AB0;\n"
"    background-color: #D5D4D4;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(291, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(1369, 16777215))
        self.tableWidget.setStyleSheet("background-color: #b2b2b2;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 4, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton_2.setMaximumSize(QtCore.QSize(133, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #00b8ef;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #626AB0;\n"
"    background-color: #D5D4D4;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(153, 243, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.action123_2 = QtWidgets.QAction(MainWindow)
        self.action123_2.setObjectName("action123_2")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мониторинга состояния корпоративной сети предприятия"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Мониторинг"))
        self.plainTextEdit.setToolTip(_translate("MainWindow", "Лог панель"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Изменение ip и данных"))
        self.pushButton_3.setText(_translate("MainWindow", "Настройка ip"))
        self.pushButton.setToolTip(_translate("MainWindow", "Пинг старт/стоп"))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ip"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Улица"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Отчистить поле лог панели"))
        self.pushButton_2.setText(_translate("MainWindow", "Отчистить"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Обновить таблицу с данными"))
        self.pushButton_6.setText(_translate("MainWindow", "Обновить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пинг ip"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action123_2.setText(_translate("MainWindow", "123"))
import res_rc
