


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
address = ('157.65.26.10', 4096)

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        with open("rog.json", 'r',encoding='UTF-8') as f:
            json_data = json.load(f)
        body_json = json.dumps(json_data, sort_keys=False,  ensure_ascii=False)
        self.wfile.write(body_json.encode("utf-8"))


    def do_POST(self):

        parsed_path = urlparse(self.path)
        content_length = int(self.headers['content-length'])
        with open('rog.json', "r",encoding='UTF-8') as json_file:
            json_data = json.load(json_file)

        json_datas = json.loads('{}'.format((self.rfile.read(content_length).decode())))
        json_data["zishin"].insert(0,json_datas)
        with open('rog.json', 'w') as outfile:
            json.dump(json_data, outfile)
    

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello from do_POST')

with HTTPServer(address, MyHTTPRequestHandler) as server:
    server.serve_forever()