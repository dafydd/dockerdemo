#!/usr/bin/python

import sys
import time
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class StubHandler(BaseHTTPRequestHandler):
  def do_GET(self):
      if self.path=='/':
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("Now                 %s\n" % time.asctime( time.localtime(time.time()) ))
        self.wfile.write("I am python version %s\n" % sys.version)
        return
      if self.path=='/other':
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("something completely different...")
        return
      if self.path=='/favicon.ico':
        self.send_error(404,'Not Found %s' % self.path)
        return
      print("ERROR: %s not found" % self.path)
      self.send_error(404,'Not Found %s' % self.path)
      return

try:
  server = HTTPServer(('', 8080), StubHandler)
  server.serve_forever()
except KeyboardInterrupt:
  print 'shutting down stubby web server'
  server.socket.close()

