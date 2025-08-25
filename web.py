from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
<head>
<title>List Of Protoclos</title>
</head>
<body bgcolor="lightyellow">
<h2 align="center">List of Protocols</h2>
<center>
<table border="1" bgcolor="lightblue" cellpadding="10">
<tr bgcolor="orange">
  <th>S. No.</th>
  <th>Name of the layer</th>
  <th>Name of the protocol</th>
</tr>
<tr>
  <td>1</td>
  <td>Application Layer</td>
  <td>HTTP, FTP, DNS, TELNET & SSH</td>
</tr>
<tr>
  <td>2</td>
  <td>Transport layer</td>
  <td>TCp/UDP</td>
</tr>
<tr>
  <td>3</td>
  <td>Network layer</td>
  <td>IPv4/IPv6</td>
</tr>
<tr>
  <td>4</td>
  <td>Link layer</td>
  <td>Ethernet</td>
</tr>
</table>
</center>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()