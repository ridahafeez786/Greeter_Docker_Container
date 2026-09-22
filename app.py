
from http.server import BaseHTTPRequestHandler, HTTPServer

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hey, my name is Rida!<br>Welcome to my Docker application!"

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = f"<h1>{message}</h1>"
        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8080), GreeterHandler)

print("Greeter app running on port 8080", flush=True)

server.serve_forever()