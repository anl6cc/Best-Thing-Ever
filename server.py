import socket
import thread

def handler(sock,addr):
    while 1:
        data = sock.recv(1024)
        if data:
            print data
    sock.close()
def sender(sock,addr):
    while True:
        data = raw_input()
        sock.sendall(data)
    sock.close()
        
if __name__=='__main__':
    HOST = "172.25.234.215"
    PORT = 5555
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.connect((HOST,PORT))
    serversock.listen(2)
    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print 'connected.'
        thread.start_new_thread(handler, (clientsock, addr))
        thread.start_new_thread(sender, (clientsock,addr))
