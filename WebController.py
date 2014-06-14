import http.server

__author__ = 'python'


def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class AquaticHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        game = 'you just lost the game'.encode()
        self.send_response(200)
        self.send_header("Content-type", 'text/plain')
        self.send_header("Content-Length", len(game))
        self.end_headers()
        self.wfile.write(game)


run(handler_class=AquaticHandler)