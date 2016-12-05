# -*- coding: utf-8 -*-

import webbrowser, json
from os.path import basename
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog

from myGui import config
from myGui import about, settings
from Connector import *


class Ui_MainWindow(object):
    def __init__(self):
        self.filename = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 568)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 568))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 568))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_test = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test.setGeometry(QtCore.QRect(30, 460, 131, 41))
        self.btn_test.setObjectName("btn_test")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 10, 391, 491))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_current_file = QtWidgets.QLabel(self.layoutWidget)
        self.label_current_file.setText("")
        self.label_current_file.setObjectName("label_current_file")
        self.horizontalLayout_2.addWidget(self.label_current_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Откройте файл или создайте новый...")
        self.textEdit.setReadOnly(True)
        self.verticalLayout_2.addWidget(self.textEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 161, 321))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_refresh = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout_3.addWidget(self.btn_refresh)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(600, 10, 391, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.text_console = QtWidgets.QPlainTextEdit(self.widget)
        self.text_console.setReadOnly(True)
        self.text_console.setObjectName("text_console")
        self.verticalLayout_4.addWidget(self.text_console)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_acts = QtWidgets.QMenu(self.menubar)
        self.menu_acts.setObjectName("menu_acts")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_open = QtWidgets.QAction(MainWindow)
        self.act_open.setObjectName("act_open")
        self.act_new = QtWidgets.QAction(MainWindow)
        self.act_new.setObjectName("act_new")
        self.act_save = QtWidgets.QAction(MainWindow)
        self.act_save.setObjectName("act_save")
        self.act_settings = QtWidgets.QAction(MainWindow)
        self.act_settings.setObjectName("act_settings")
        self.act_exit = QtWidgets.QAction(MainWindow)
        self.act_exit.setObjectName("act_exit")
        self.act_about = QtWidgets.QAction(MainWindow)
        self.act_about.setObjectName("act_about")
        self.act_help = QtWidgets.QAction(MainWindow)
        self.act_help.setObjectName("act_help")
        self.act_refresh = QtWidgets.QAction(MainWindow)
        self.act_refresh.setObjectName("act_refresh")
        self.act_test = QtWidgets.QAction(MainWindow)
        self.act_test.setObjectName("act_test")
        self.act_close = QtWidgets.QAction(MainWindow)
        self.act_close.setObjectName("act_close")
        self.act_just_save = QtWidgets.QAction(MainWindow)
        self.act_just_save.setObjectName("act_just_save")
        self.menu_file.addAction(self.act_new)
        self.menu_file.addAction(self.act_open)
        self.menu_file.addAction(self.act_just_save)
        self.menu_file.addAction(self.act_save)
        self.menu_file.addAction(self.act_close)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_exit)
        self.menu_options.addAction(self.act_settings)
        self.menu_help.addAction(self.act_about)
        self.menu_help.addAction(self.act_help)
        self.menu_acts.addAction(self.act_refresh)
        self.menu_acts.addAction(self.act_test)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_acts.menuAction())
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(-1)
        self.btn_test.clicked.connect(self.act_test.trigger)
        self.btn_refresh.clicked.connect(self.act_refresh.trigger)
        self.act_exit.triggered.connect(MainWindow.close)

        self.act_new.triggered.connect(self.new_file)
        self.act_open.triggered.connect(self.open_file)
        self.act_save.triggered.connect(self.save_file_as)
        self.act_just_save.triggered.connect(self.save_file)
        self.act_close.triggered.connect(self.close)

        self.act_test.triggered.connect(self.test)
        self.act_refresh.triggered.connect(self.refresh_list)

        self.act_settings.triggered.connect(self.settings)

        self.act_about.triggered.connect(self.about)
        self.act_help.triggered.connect(self.show_help)

        self.__set_font__(config["FONT"]["value"])

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестирование"))
        self.btn_test.setText(_translate("MainWindow", "Тестировать"))
        self.label_2.setText(_translate("MainWindow", "Тестовые данные:"))
        self.label.setText(_translate("MainWindow", "Список тестов:"))
        self.btn_refresh.setText(_translate("MainWindow", "Обновить"))
        self.label_3.setText(_translate("MainWindow", "Консоль:"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_options.setTitle(_translate("MainWindow", "Опции"))
        self.menu_help.setTitle(_translate("MainWindow", "Справка"))
        self.menu_acts.setTitle(_translate("MainWindow", "Действия"))
        self.act_open.setText(_translate("MainWindow", "Открыть"))
        self.act_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.act_new.setText(_translate("MainWindow", "Новый"))
        self.act_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.act_save.setText(_translate("MainWindow", "Сохранить как..."))
        self.act_save.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.act_settings.setText(_translate("MainWindow", "Настройки"))
        self.act_settings.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.act_exit.setText(_translate("MainWindow", "Выход"))
        self.act_about.setText(_translate("MainWindow", "О программе"))
        self.act_about.setShortcut(_translate("MainWindow", "F1"))
        self.act_help.setText(_translate("MainWindow", "Справка"))
        self.act_help.setShortcut(_translate("MainWindow", "Ctrl+F1"))
        self.act_refresh.setText(_translate("MainWindow", "Обновить список тестов"))
        self.act_refresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.act_test.setText(_translate("MainWindow", "Тестировать"))
        self.act_test.setShortcut(_translate("MainWindow", "Return"))
        self.act_close.setText(_translate("MainWindow", "Закрыть текущий файл"))
        self.act_close.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.act_just_save.setText(_translate("MainWindow", "Сохранить"))
        self.act_just_save.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def __set_font__(self, font_string):
        font = QtGui.QFont()
        font.fromString(font_string)
        self.textEdit.setFont(font)
        self.text_console.setFont(font)

    def __validate_json__(self):
        try:
            json.loads(self.textEdit.toPlainText())
        except ValueError as e:
            self.statusbar.showMessage("ER+! Json не прошел валидацию: " + str(e))
            return False

        return True

    # """"""""""""""""""
    # File-menu handlers
    # """"""""""""""""""
    def new_file(self):
        self.label_current_file.setText("Untitled.json")
        self.textEdit.setReadOnly(False)
        self.textEdit.setPlaceholderText("Заполните тестовые данные...")
        self.statusbar.showMessage("Создан новый файл")
        self.filename = "./Untitled.json"

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Открыть файл", "", "JSON-файлы (*.json)")
        if filename != "":
            with open(filename, 'r', encoding='utf-8') as file:
                data = file.read()
            self.textEdit.setText(data)
            self.filename = filename

            self.statusbar.showMessage("Открыт файл: " + filename)
            self.textEdit.setReadOnly(False)
            self.label_current_file.setText(basename(filename))

    def save_file(self):
        if self.filename != "":
            if self.__validate_json__():
                with open(self.filename, "w", encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
                self.statusbar.showMessage("Файл успешно сохранен.")
            else:
                self.statusbar.showMessage("ER+! JSON не прошел валидацию.")

    def save_file_as(self):
        if self.__validate_json__():

            filename, _ = QFileDialog.getSaveFileName(None, "Сохранить как", "", "JSON-файлы (*.json)")

            if filename != "":
                data = self.textEdit.toPlainText()

                with open(filename, "w", encoding='utf-8') as file:
                    file.write(data)

                self.statusbar.showMessage("Успешное сохранение файла: " + filename)
                self.label_current_file.setText(basename(filename))

    def close(self):
        if self.textEdit.isReadOnly():
            return

        title = 'Закрыть текущий файл?'
        message = 'Вы действительно хотите закрыть текущий файл? Все несохраненные изменения будут потеряны.'
        reply = QMessageBox.question(None, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.textEdit.setPlainText("")
            self.textEdit.setReadOnly(True)
            self.textEdit.setPlaceholderText("Откройте файл или создайте новый...")
            self.label_current_file.setText("")
            self.statusbar.showMessage("Файл был закрыт успешно.")

    # """""""""""""""""""""
    # Actions-menu handlers
    # """""""""""""""""""""
    def refresh_list(self):
        try:
            connector = Connector(config["DEFAULT"]["url"], '/' + config["DEFAULT"]["suburl"] + "/")
            test_list = connector.get_test_list()
            self.listWidget.clear()
            print("\nCurrent test_list:")
            print(test_list)

            for test in test_list:
                self.listWidget.addItem(test)

            self.statusbar.showMessage("Список доступных тестов был обновлен.")
        except Exception as e:
            self.statusbar.showMessage(str(e))
            QMessageBox.warning(None, "Ошибка", str(e), QMessageBox.Ok)

    def test(self):
        if self.label_current_file.text() == "":
            self.statusbar.showMessage("ER+! Откройте файл, прежде чем тестировать")

        elif self.textEdit.toPlainText() == "":
            self.statusbar.showMessage("ER+! Окно данных пусто!")

        elif not self.__validate_json__():
            self.statusbar.showMessage("ER+! JSON не прошел валидацию...")

        elif self.listWidget.currentRow() == -1:
            self.statusbar.showMessage("ER+! Не выбран тест из списка")

        else:
            self.statusbar.showMessage("Тестирование...")
            test_name = self.listWidget.currentItem().text()
            data = {
                "name": test_name,
                "send": "on",
                "test_data": self.textEdit.toPlainText(),
                "python": "true"
            }

            result = "-------------------------------\n"
            result += "Создание соединения.\n"
            try:
                connector = Connector(config["DEFAULT"]["url"], '/' + config["DEFAULT"]["suburl"] + "/")
                result += "Соединение создано успешно.\n"

                result += "Выполняется запрос к серверу. Ожидание ответа сервера.\n\n"
                request = connector.test_request(data)

                result += "Ответ сервера получен:\n"
                result += "Reason: \"" + request.get("Reason") + "\". Status: " + str(request.get("Status")) + "\n"
                result += "Data:\n" + request.get("Data")
                self.text_console.setPlainText(result)

            except Exception as e:
                result += "Произошла непредвиденная ошибка."
                self.text_console.appendPlainText(result)
                QMessageBox.warning(None, "Ошибка", str(e), QMessageBox.Ok)

            self.statusbar.showMessage("Подключение к серверу завершено!")



    # """""""""""""""""""""
    # Options-menu handlers
    # """""""""""""""""""""
    def settings(self):
        self.statusbar.showMessage('Вызвано диалоговое окно "Настройки"')
        settings_window = QDialog()
        ui = settings.Ui_Dialog()
        ui.setupUi(settings_window)

        settings_window.setModal(True)

        if settings_window.exec_():
            with open("config.ini", "w") as cfg_file:
                config.write(cfg_file)

            self.__set_font__(config['FONT']['value'])

            self.statusbar.showMessage('Настройки обновлены')
        else:
            self.statusbar.showMessage('')

    # """""""""""""""""""""
    # Help-menu handlers
    # """""""""""""""""""""
    def about(self):
        self.statusbar.showMessage('Вызвано диалоговое окно "О программе"')
        about_window = QDialog()
        ui = about.Ui_Dialog()
        ui.setupUi(about_window)

        about_window.setModal(True)
        about_window.exec()
        self.statusbar.showMessage('')

    def show_help(self):
        webbrowser.open("http://localhost/view/pages/help_common.php")
