import socket
import os

UDP_IP = "192.168.10.4"
UDP_PORT = 5005
#dir_path = os.path.dirname(os.path.realpath(__file__))

MESSAGE = "hello world"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "message: ", MESSAGE

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data = sock.recv(1024)

print ('Received', repr(data))
