
import ipaddress
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from db import connect_db

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 385)
        Form.setMinimumSize(QtCore.QSize(691, 385))
        Form.setMaximumSize(QtCore.QSize(691, 385))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/Python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        #self.label = QtWidgets.QLabel(Form)
        self.label = MyLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 391))
        self.label.setStyleSheet("border-image: url(:/img/Снимок.PNG);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(450, 274, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(15)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 295, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 316, 241, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 337, 241, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 360, 75, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"                         background-color: #54e346;\n"
"                         }\n"
"                         QPushButton:hover {\n"
"                         background-color: white;\n"
"                         }\n"
"                         QPushButton:pressed {\n"
"                         color: #626AB0;\n"
"                         background-color: #D5D4D4;\n"
"                         }")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление нового участка"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Введите ip"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Введите организацию"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Введите улицу"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Введите город"))
        self.pushButton.setText(_translate("Form", "Ok"))
import res_rc


class MyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

    def mouseReleaseEvent(self, event):
        #if event.button() == Qt.LeftButton and self.parent.flag:
            self._pos = event.pos()
            #print(f'def mouseReleaseEvent(self, event): {event.pos()} <----')
            qss = """QLabel {background-color: #fff;
                        border-radius: 5px;
                        min-height: 10px;
                        max-height: 10px;
                        min-width: 10px;
                        max-width: 10px;
                        border-style: solid;
                        border-color: black;
                        border-width: 1px;}
               """
            self.parent.label_pos.setText(
                f"<b style='color: #fff; font-size: 12px'>. x:{self._pos.x()}, y:{self._pos.y()-10}</b>")
            self.parent.label_pos.move(self._pos.x(), self._pos.y()-10)
            self.parent.label_pos.adjustSize()
            self.parent.flag = True

            self.parent.coordX = self._pos.x()       
            self.parent.coordY = self._pos.y()-10
            

class MyWin(QtWidgets.QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.coordX = None
        self.coordY = None
        
        self.label_pos = QLabel(self)

        self.pushButton.clicked.connect(self.add_new_label)

    def add_new_label(self):
        text = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        text3 = self.lineEdit_3.text()
        text4 = self.lineEdit_4.text()

        if text and text2 and text3 and text4:

            try:
                if ipaddress.ip_address(text):
                    recor = connect_db("""SELECT INET_NTOA(ip) FROM ips""", 'all')
                    
                    self.indentify = True
                    
                    for i in recor:                
                        if text in i:
                            self.indentify = False
                            msg = QMessageBox.information(self, 'Внимание', 'Такой ip уже существует!')
                    
                    if self.indentify:                                     
                        if self.coordX and self.coordY:
                            recor = connect_db("""SELECT id FROM ips""", 'all')
                            
                            connect_db(f"""INSERT INTO ips (id, Gor, Yi, Location, ip, x, y) VALUES ({max(recor)[0]+1}, "{text4}", "{text3}", "{text2}", INET_ATON("{text}"), {self.coordX}, {self.coordY})""", 'commit')

                            msg = QMessageBox.information(self, "Внимание", "Данные добавлены!")

                            self.lineEdit.clear()
                            self.lineEdit_2.clear()
                            self.lineEdit_3.clear()
                            self.lineEdit_4.clear()
                        
                        else:
                            msg = QMessageBox.information(self, 'Внимание', 'Отметьте точку координат!')

            except ValueError:
                msg = QMessageBox.information(self, 'Внимание', 'Введён не корректный ip адрес!')
        else:
            msg = QMessageBox.information(self, 'Внимание', 'Заполните все поля!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())