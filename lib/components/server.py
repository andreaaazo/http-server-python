from http.server import HTTPServer
from .request_handler import Handler
from settings import *


class Server(HTTPServer):
    def __init__(self):
        server_address = (HOSTNAME, PORT)
        RequestHandlerClass = Handler
        super().__init__(server_address, RequestHandlerClass)
