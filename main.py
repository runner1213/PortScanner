import ipaddress
import os
import subprocess
import socket

import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "resources", "sayoriicon.ico")
        window.setWindowIcon(QIcon(icon_path))
        window.resize(800, 600)
        window.setStyleSheet("    QWidget {\n"
"        background-color: #121212; /* Тёмный фон окна */\n"
"        color: #E0E0E0; /* Светлый текст */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #E0E0E0; /* Белый текст */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333; /* Тёмно-серый фон */\n"
"    color: #E0E0E0; /* Белый текст */\n"
"    border: 1px solid #444444; /* Серый контур */\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444444; /* Светлее при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Темнее при нажатии */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=window)
        self.centralwidget.setObjectName("centralwidget")
        self.start_scanBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_scanBtn.setGeometry(QtCore.QRect(180, 440, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.start_scanBtn.setFont(font)
        self.start_scanBtn.setObjectName("start_scanBtn")
        self.minPort = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.minPort.setGeometry(QtCore.QRect(500, 250, 111, 31))
        self.minPort.setMinimum(1)
        self.minPort.setMaximum(65535)
        self.minPort.setObjectName("minPort")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(500, 330, 111, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(65535)
        self.spinBox.setObjectName("spinBox")
        self.locationofip = QtWidgets.QLabel(parent=self.centralwidget)
        self.locationofip.setGeometry(QtCore.QRect(40, 370, 400, 28))
        self.locationofip.setObjectName("locationofip")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startportlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.startportlabel.setGeometry(QtCore.QRect(360, 250, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.startportlabel.setFont(font)
        self.startportlabel.setObjectName("startportlabel")
        self.endportlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.endportlabel.setGeometry(QtCore.QRect(370, 330, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.endportlabel.setFont(font)
        self.endportlabel.setObjectName("endportlabel")
        self.EnterDomain = QtWidgets.QLabel(parent=self.centralwidget)
        self.EnterDomain.setGeometry(QtCore.QRect(40, 250, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.EnterDomain.setFont(font)
        self.EnterDomain.setObjectName("EnterDomain")
        self.ipofdomain = QtWidgets.QLabel(parent=self.centralwidget)
        self.ipofdomain.setGeometry(QtCore.QRect(40, 346, 161, 20))
        self.ipofdomain.setObjectName("ipofdomain")
        self.plainTextEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 280, 181, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.checkDomain = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkDomain.setGeometry(QtCore.QRect(120, 320, 81, 27))
        self.checkDomain.setObjectName("checkDomain")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

        self.start_scanBtn.clicked.connect(self.on_start_scanBtn_click)
        self.checkDomain.clicked.connect(self.on_checkDomainBtn_click)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "PortScanner"))
        self.start_scanBtn.setText(_translate("window", "Начать сканирование"))
        self.label.setText(_translate("window", "Сканер портов"))
        self.startportlabel.setText(_translate("window", "Начальный порт"))
        self.endportlabel.setText(_translate("window", "Конечный порт"))
        self.EnterDomain.setText(_translate("window", "Введите домен для скана"))
        self.ipofdomain.setText(_translate("window", "Айпи: "))
        self.checkDomain.setText(_translate("window", "Проверить"))
        self.locationofip.setText(_translate("window", "Локация: "))

    def get_location(self, ip):
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            country = data["country"]
            city = data["city"]
            region = data["regionName"]
            return f"{country}, {city}, {region}"
        else:
            return "Не удалось определить локацию."

    def on_checkDomainBtn_click(self):
        domain = self.plainTextEdit.text()
        try:
            ip_address = socket.gethostbyname(domain)
            self.ipofdomain.setText(f"Айпи: {ip_address}")
            location = self.get_location(ip_address)
            self.locationofip.setText(f"Локация: {location}")
        except socket.error as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка: {str(e)}")

    @staticmethod
    def is_valid_ipv4(self, ip):
        try:
            ip_obj = ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    def on_start_scanBtn_click(self):
        """domain = self.plainTextEdit.text()
        try:
            ip_address = socket.gethostbyname(domain)
        except socket.error as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка: {str(e)}")
            return
            """
        domain = self.plainTextEdit.text()
        start_port = self.minPort.value()
        end_port = self.spinBox.value()

        if self.is_valid_ipv4(self, domain):
            try:
                self.ipofdomain.setText(f"Айпи: {domain}")
            except socket.error as e:
                QMessageBox.critical(None, "Ошибка", f"Ошибка: {str(e)}")
                return
            location = self.get_location(domain)
            self.locationofip.setText(f"Локация: {location}")
        else:
            try:
                ip_address = socket.gethostbyname(domain)
                self.ipofdomain.setText(f"Айпи: {ip_address}")
            except socket.error as e:
                QMessageBox.critical(None, "Ошибка", f"Ошибка: {str(e)}")
                return
            location = self.get_location(ip_address)
            self.locationofip.setText(f"Локация: {location}")

        # Окно выбора количества потоков
        threads, ok = QtWidgets.QInputDialog.getInt(None, "Выбор потоков", "Введите количество потоков:", 50, 1, 1000)
        if not ok:
            return
        if threads > 800:
            QMessageBox.warning(None, "Предупреждение", "Выбранное вами количество используемых потоков слишком большое. Продолжайте с осторожностью.")

        # Запуск консольного сканера
        exe_dir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.getcwd()
        portconsole_path = os.path.join(exe_dir, "portconsole.py")
        subprocess.Popen(["python", portconsole_path, domain, str(start_port), str(end_port), str(threads)],
                         creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
