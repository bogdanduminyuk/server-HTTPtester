# coding: utf-8
from http.client import HTTPConnection
from urllib import parse


class Connector:
    def __init__(self, url, sub_url):
        self.connection = HTTPConnection(url)
        self.sub_url = sub_url

    def __del__(self):
        self.connection.close()

    def test_request(self, data):
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        data = parse.urlencode(data)

        self.connection.request("POST", self.sub_url, data, headers)
        response = self.connection.getresponse()

        return {"Status" : response.status, "Reason" : response.reason, "Data" : response.read().decode('utf-8')}

    def get_test_list(self):
        pass
