from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)


def task(name):
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    task('main')
