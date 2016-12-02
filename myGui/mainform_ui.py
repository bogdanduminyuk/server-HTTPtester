# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 568)
        MainWindow.setMinimumSize(QtCore.QSize(600, 568))
        MainWindow.setMaximumSize(QtCore.QSize(600, 568))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_test = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test.setGeometry(QtCore.QRect(30, 460, 131, 41))
        self.btn_test.setObjectName("btn_test")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 10, 391, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 161, 321))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.widget1)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_refresh = QtWidgets.QPushButton(self.widget1)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout_3.addWidget(self.btn_refresh)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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
        self.menu_file.addAction(self.act_new)
        self.menu_file.addAction(self.act_open)
        self.menu_file.addAction(self.act_save)
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
        self.listWidget.setCurrentRow(1)
        self.btn_test.clicked.connect(self.act_test.trigger)
        self.btn_refresh.clicked.connect(self.act_refresh.trigger)
        self.act_exit.triggered.connect(MainWindow.close)
        self.act_open.triggered.connect(self.open_file)
        self.act_refresh.triggered.connect(self.refresh_list)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_test.setText(_translate("MainWindow", "Тестировать"))
        self.label_2.setText(_translate("MainWindow", "Тестовые данные:"))
        self.label.setText(_translate("MainWindow", "Список тестов:"))
        self.btn_refresh.setText(_translate("MainWindow", "Обновить"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_options.setTitle(_translate("MainWindow", "Опции"))
        self.menu_help.setTitle(_translate("MainWindow", "Справка"))
        self.menu_acts.setTitle(_translate("MainWindow", "Действия"))
        self.act_open.setText(_translate("MainWindow", "Открыть"))
        self.act_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.act_new.setText(_translate("MainWindow", "Новый"))
        self.act_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.act_save.setText(_translate("MainWindow", "Сохранить"))
        self.act_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
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

    def open_file(self):
        dlg = QFileDialog()
        if dlg.exec_():
            self.filename = dlg.selectedFiles()
            print(self.filename)

    def refresh_list(self):
        self.listWidget.addItem("qwerty")
