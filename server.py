import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost',8089))
serversocket.listen(5)

while True:
    conn, addr = serversocket.accept()
    print "got connection from",addr
    msg = conn.recv(64)
    if len(msg) > 0:
        print "received:",msg
	conn.send(msg)
