import socket
import os

HOST = '127.0.0.1'
PORT = 65432
#dir_path = os.path.dirname(os.path.realpath(__file__))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open("test_file.txt", "r") as f:
        f.readline()
        for line in f:
            b = bytearray(line, "utf-8")
            s.sendall(b)
            data = s.recv(1024)
    f.close

print ('Received', repr(data))