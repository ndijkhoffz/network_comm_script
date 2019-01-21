import socket
import os

UDP_IP = "192.168.10.3"
UDP_PORT = 50005

#dir_path = os.path.dirname(os.path.realpath(__file__))

MESSAGE = "hello world"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "message: ", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data = sock.recv(1024)

print "Received", repr(data)
