# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from myGui.mainform import Ui_MainWindow

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(window)
        ui.refresh_list()
        window.show()

        sys.exit(app.exec_())

    except Exception as e:
        print(type(e))
        print(e)
