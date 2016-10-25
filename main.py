# coding: utf-8
from argparse import ArgumentParser
import httpConnector

def initArgs():
    parser = ArgumentParser(description="It is a program for running php-tests by using http-queries.")
    parser.add_argument("URL", type=str, help="url to parse")
    parser.add_argument("-v", "--verbose", action="store_true", help="The argument is used to enable logging in console")
    return parser.parse_args()

if __name__ == "__main__":
    args = initArgs()
    print(args)
