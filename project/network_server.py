# import the socket module
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s is the socket object used to listen for new connections
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    # conn is used to send data to the client
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)