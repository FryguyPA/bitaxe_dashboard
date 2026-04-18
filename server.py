#!/usr/bin/env python3
"""
BitAxe Dashboard proxy server.
Serves dashboard.html and proxies /proxy/<ip>/api/... requests to miners,
bypassing browser CORS restrictions.

Usage:
    python3 server.py          # listens on http://localhost:8080
    python3 server.py 9000     # custom port
"""

import sys
import os
import json
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
PROXY_PREFIX = "/proxy/"


class DashboardHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # Suppress noisy access logs; only show proxy activity
        if self.path.startswith(PROXY_PREFIX):
            print(f"  proxy → {self.path[len(PROXY_PREFIX):]}")

    def do_GET(self):
        if self.path.startswith(PROXY_PREFIX):
            self._handle_proxy()
        else:
            super().do_GET()

    def do_OPTIONS(self):
        # Pre-flight for any path
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def _handle_proxy(self):
        # Path format: /proxy/<ip-or-host>/api/system/info
        tail = self.path[len(PROXY_PREFIX):]  # e.g. "192.168.5.79/api/system/info"
        target_url = f"http://{tail}"

        req = urllib.request.Request(
            target_url,
            headers={"Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                body = resp.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except urllib.error.URLError as e:
            reason = str(e.reason) if hasattr(e, "reason") else str(e)
            body = json.dumps({"error": reason}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            body = json.dumps({"error": str(e)}).encode()
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(("", PORT), DashboardHandler)
    print(f"BitAxe Dashboard → http://localhost:{PORT}/dashboard.html")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
