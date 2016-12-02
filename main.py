# coding: utf-8

import sys
from Connector import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from myGui.mainform_ui import Ui_MainWindow

if __name__ == "__main__":
    url = 'localhost'
    subUrl = '/lib/test/'
    testName = "TextProcessorTest.php"
    
    data = parse.urlencode({
        "name" : testName,
        "send" : "on",
    })

    data = {
        "name" : testName,
        "send" : "on",
        "test_data":
            '''{"testIsUrl": {
                "http://google.ru": 1,
                "https:///cSAdASCZXCV1qwerty": 0,
                "https://www.yandex.ru": 1,
                "htp://qwerty.loc": 1
            },

            "testTranslit": {
                "привет": "privet",
                "пока": "poka",
                "Маша": "Masha"
            },

            "testRemovingSpaceSymbols": {

            }
        }'''
        
        # форма для создания тестового файла (или динамических тестовых данных)
        # 

    }

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}    
    
    try:
        """conn = Connector(url, subUrl)
        res = conn.test_request(data)
        # res = conn.get_test_list()
        print(res.get("Data"))"""

        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(type(e))
        print(e)
