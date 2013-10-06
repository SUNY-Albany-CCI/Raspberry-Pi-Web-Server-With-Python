import SocketServer
import MyCameraHandlerREST

PORT = 8000

Handler = MyCameraHandlerREST.MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
