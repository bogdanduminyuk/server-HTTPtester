# coding: utf-8
from argparse import ArgumentParser
from PyQt5 import *

from Connector import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def init_args():
    parser = ArgumentParser(description="It is a program for running php-tests by using http-queries.")
    parser.add_argument("URL", type=str, help="url to parse")
    parser.add_argument("-v", "--verbose", action="store_true", help="The argument is used to enable logging in console")
    return parser.parse_args()

if __name__ == "__main__":
    # args = init_args()
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

        w = QWidget()
        w.resize(250, 150)
        w.move(300, 300)
        w.setWindowTitle('Дарова')
        w.show()

        sys.exit(app.exec_())

    except Exception as e:
        print(type(e))
        print(e)
