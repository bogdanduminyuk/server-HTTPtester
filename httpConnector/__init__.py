# coding: utf-8
from http.client import HTTPConnection
import shutil, time

class HTTPConnector:
    
    def __init__(self, url, data, headers):
        self.connection = HTTPConnection(url)
        self.connection.request("POST", "/home/include/script/generate_empty_template.php", data, headers)
        response = self.connection.getresponse()
        out_file = open("/home/bogdan/" + str(time.time()) + ".zip", 'wb')
        shutil.copyfileobj(response, out_file)

        print(type(response))
        print(response.getheader("Content-disposition"))