from http.server import HTTPServer

from .http_request_handler import HTTPRequestHandler

from settings import *


class Server(HTTPServer):
    def __init__(self):
        server_address = (HOSTNAME, PORT)
        RequestHandlerClass = HTTPRequestHandler
        super().__init__(server_address, RequestHandlerClass)
