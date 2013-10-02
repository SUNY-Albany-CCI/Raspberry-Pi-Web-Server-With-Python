import SocketServer
import MyCameraHandler

PORT = 8000

Handler = MyCameraHandler.MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
