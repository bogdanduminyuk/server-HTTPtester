# coding: utf-8
from argparse import ArgumentParser
from httpConnector import HTTPConnector
import urllib


def initArgs():
    parser = ArgumentParser(description="It is a program for running php-tests by using http-queries.")
    parser.add_argument("URL", type=str, help="url to parse")
    parser.add_argument("-v", "--verbose", action="store_true", help="The argument is used to enable logging in console")
    return parser.parse_args()

if __name__ == "__main__":
    args = initArgs()
    
    data = urllib.parse.urlencode({
        "title" : "qwerty",
        "jquery" : "on",
        "description" : "description",
        "send" : "on",
    })

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}    
    
    try:
        cn = HTTPConnector(args.URL, data, headers)
        
    except Exception as e:
        print(type(e))
        print(e)
