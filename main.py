# coding: utf-8
from argparse import ArgumentParser
from http.client import HTTPConnection
from urllib import parse

from Connector import *


def init_args():
    parser = ArgumentParser(description="It is a program for running php-tests by using http-queries.")
    parser.add_argument("URL", type=str, help="url to parse")
    parser.add_argument("-v", "--verbose", action="store_true", help="The argument is used to enable logging in console")
    return parser.parse_args()

if __name__ == "__main__":
    # args = init_args()
    url = 'localhost'
    subUrl = '/test/'
    testName = "TextProcessorTest.php"
    
    data = parse.urlencode({
        "name" : testName,
        "send" : "on",
    })

    data = {
        "name" : testName,
        "send" : "on",
    }

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}    
    
    try:
        """connection = HTTPConnection(url)
        connection.request("POST", subUrl, data, headers)
        response = connection.getresponse()

        data = response.read()
        status = response.status
        reason = response.reason
        data = data.decode("utf-8")

        connection.close()
        print("Status=",status)
        print("Reason=", reason)
        print(data)"""

        conn = Connector(url, subUrl)
        #res = conn.test_request(data)
        res = conn.get_test_list()
        print(res)

        
    except Exception as e:
        print(type(e))
        print(e)
