# coding: utf-8
from http.client import HTTPConnection
from urllib import parse


class Connector:
    def __init__(self, url, sub_url):
        self.connection = HTTPConnection(url)
        self.sub_url = sub_url
        self.headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    def __del__(self):
        self.connection.close()

    def test_request(self, data):
        data = parse.urlencode(data)

        self.connection.request("POST", self.sub_url, data, self.headers)
        response = self.connection.getresponse()

        return {"Status" : response.status, "Reason" : response.reason, "Data" : response.read().decode('utf-8')}

    def get_test_list(self):
        data = {'list' : '1'}

        response = self.test_request(data)
        result = response.get("Data").split(";")
        result.pop()

        return result

