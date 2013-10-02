import SocketServer
import MyHandler

PORT = 8000

Handler = MyHandler.MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
