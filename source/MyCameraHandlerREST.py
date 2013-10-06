import SimpleHTTPServer
import urlparse
import subprocess

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

  def do_GET(self):

    parsedParameters = urlparse.urlparse(self.path)
    queryParsed = urlparse.parse_qs(parsedParameters.query)

    if 'filename' in queryParsed:

      width = queryParsed.get('width',['300'])[0]
      height = queryParsed.get('height',['300'])[0]
      timeout = queryParsed.get('timeout',['500'])[0]
      filename = queryParsed.get('filename',['image.jpg'])[0]

      subprocess.call(["raspistill","-n",
         "--width",width,
         "--height",height,
         "--timeout",timeout,
         "-o",filename])

      self.processMyRequest(filename)

    else:

      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);


  def processMyRequest(self, filename):

    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()

    self.wfile.write("<!DOCTYPE html>\n")
    self.wfile.write("<html>\n")
    self.wfile.write("<body>\n")
    self.wfile.write("<h1>Image: " + filename + "</h1>\n")
    self.wfile.write('<img src="./'+filename+'" alt="camera">\n')
    self.wfile.write("</body>\n")
    self.wfile.write("</html>\n")
    self.wfile.close()

