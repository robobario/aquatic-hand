import http.server

__author__ = 'python'


def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class AquaticHandler(http.server.BaseHTTPRequestHandler):
    def serve_file(self, html):
        f = open(html)
        flines = '\n'.join(f.readlines())
        game = flines.encode()
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.send_header("Content-Length", len(game))
        self.end_headers()
        self.wfile.write(game)

    def do_GET(self):
        if self.path == "/":
            self.serve_file('aquatic.html')
        elif self.path == "/aquatic.js":
            self.serve_file('aquatic.js')



run(handler_class=AquaticHandler)