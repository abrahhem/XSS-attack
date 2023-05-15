import http.server

from Model import Model
from View import View
from Controller import Controller

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.model = Model("comments.txt", "users.txt")
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.controller.handle_request(self)

    def do_POST(self):
        self.controller.handle_request(self)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    print(f'Starting server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
