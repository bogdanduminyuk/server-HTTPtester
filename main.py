# coding: utf-8
from argparse import ArgumentParser
from http.client import HTTPConnection
import urllib


def initArgs():
    parser = ArgumentParser(description="It is a program for running php-tests by using http-queries.")
    parser.add_argument("URL", type=str, help="url to parse")
    parser.add_argument("-v", "--verbose", action="store_true", help="The argument is used to enable logging in console")
    return parser.parse_args()

if __name__ == "__main__":
    #args = initArgs()
    url = 'localhost'
    subUrl = '/test/'
    
    data = urllib.parse.urlencode({
        "name" : "TextProcessorTest.php",
        "send" : "on",
    })

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}    
    
    try:
        connection = HTTPConnection(url)
        connection.request("POST", subUrl, data, headers)
        response = connection.getresponse()

        data = response.read()
        status = response.status
        reason = response.reason
        data = data.decode("utf-8")

        connection.close()
        print("Status=",status)
        print("Reason=", reason)
        print(data)
        
    except Exception as e:
        print(type(e))
        print(e)
