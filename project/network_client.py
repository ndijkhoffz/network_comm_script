import socket
import os

UDP_IP = "192.168.10.4"
UDP_PORT = 50005

#@TODO: there should be a main command interface
#       that can receive commands when program is
#       running to determine if sending or requesting:
#       data.

#PATH for reading the file and where to write the file received.

#dir_path = os.path.dirname(os.path.realpath(__file__))

MESSAGE_UDP = "hello world how are you"
MESSAGE_TCP = "this is a tcp message not a udp message"
#@TODO: here we should open the file to be sent and
#       read out to the buffer to be used for sending
#       to the server.


#@TODO: Process request from user and perform either
#       transmit or request.

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
#print "message: ", MESSAGE_TCP

location = os.getcwd()
print location

print "Task options::"
print "Read out data = R"
print "Write data = W"
cmd = raw_input("Please select a task:")
if cmd == "W" or cmd == "w":    
    #f = open("/devel/test_data/test_file_100M")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.sendall(MESSAGE_TCP)
    print "Sending message!"
    with open("test_file_100M.dat", "r") as fd:
        for line in fd:
            #print "Sending message..."
	    #print line
            sock.sendto(line, (UDP_IP, UDP_PORT))
            #print "Message sent!"
            #print "Waiting for response..."
            #data = sock.recv(1024)
    print "Done!"
    #print "Received", repr(data)
#else if cmd == "R" or cmd == "r"
   #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
