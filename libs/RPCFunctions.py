import math
import http.client

class RPCFunctions:
    def __init__(self):
        pass

    def add(self, a, b):
        if not a or not b: return
        return a + b

    def is_even(self, n):
        if not n: return
        return not n & 1

    def is_prime(self, n):
        if not n: return
        div = 0
        for i in range(1, n):
            if n % i == 0:
                div += 1
        return div < 2

    def is_even_xml(self, n):
        if not n: return
        request_str = "<?xml version='1.0'?>\n<methodCall>\n<methodName>is_even</methodName>\n<params>\n<param>\n<value><int>3</int></value>\n</param>\n</params>\n</methodCall>\n"
        request_body = request_str.encode()
        try:
            connection = http.client.HTTPConnection('localhost:12345')
            connection.putrequest('POST', '/')
            connection.putheader('Content-Type', 'text/xml')
            connection.putheader('User-Agent', 'Python-xmlrpc/3.5')
            connection.putheader("Content-Length", str(len(request_body)))
            connection.endheaders(request_body)

            return connection.getresponse().read()
        except ValueError:
            return ValueError
