import SimpleHTTPServer
import urlparse
import subprocess

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

  def do_GET(self):

    parsedParameters = urlparse.urlparse(self.path)
    queryParsed = urlparse.parse_qs(parsedParameters.query)

    subprocess.call(["raspistill","-n",
       "--width","300","--height","300",
       "--timeout","50","-o","image.jpg"])

    if ( 'name' in queryParsed ):
      self.processMyRequest(queryParsed)
    else:
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);





  def processMyRequest(self, query):

    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()

    nameString = query['name']
    clientAddress = self.client_address[0]

    if nameString[0]:
      self.wfile.write("<!DOCTYPE html>")
      self.wfile.write("<html>")
      self.wfile.write("<body>")
      self.wfile.write("<h1>Welcome " + nameString[0] + "</h1>")
      self.wfile.write("<h2>from " + clientAddress + "</h2>")
      self.wfile.write('<img src="image.jpg" alt="camera">"')
      self.wfile.write("</body>")
      self.wfile.write("</html>")
      self.wfile.close()

