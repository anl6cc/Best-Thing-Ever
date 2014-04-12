import socket
import sys

HOST, PORT = "172.25.200.121", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data + "\n")

        # Receive data from the server and shut down
        while True:
            received = sock.recv(1024)
            if len(received) > 0:
                print received
                break;
    finally:
        sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
