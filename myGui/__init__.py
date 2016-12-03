# coding: utf-8

import configparser

config = configparser.ConfigParser()
config.read("config.ini")
print('Current URL: ', config["DEFAULT"]['url'])
print('Current SubURL: ', config["DEFAULT"]['suburl'])