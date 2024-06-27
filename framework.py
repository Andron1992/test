import http.server

class GoITHTTPHandler(http.server.BaseHTTPRequestHandler):
    def _process_request(self, method: str):
        logger