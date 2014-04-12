import SocketServer

IPList = []
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        if self.client_address[0] not in IPList: IPList.append(self.client_address[0])
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        print type(self.request)
        # just send back the same data, but upper-cased
        for x in self.client_address[0]:
            #self.request.sendall(self.data.upper())
            if x != original_client:
                self.request.sendto(self.data,x)

if __name__ == "__main__":
    HOST, PORT = "172.25.200.121", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
