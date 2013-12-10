#!/usr/bin/python

import sys
from BaseHTTPServer import HTTPServer as SC
from SimpleHTTPServer import SimpleHTTPRequestHandler as HC

P = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 9000
server = ('0.0.0.0', port)
HC.protocol_version = P
httpd = SC(server, HC)

s = httpd.socket.getsockname()
print "El servidor esta corriendo sobre ", s[0], "puerto", s[1] 

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

