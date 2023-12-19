#UDP Server side

import socket

#Create a server side socket IPV4 (AF_INET) and UPD (SOCKET_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind our new socket to a tuple (IP address, prot address)
ip_addr = socket.gethostbyname(socket.gethostname())
server_socket.bind((ip_addr, 12345))

#We are not llistening or accepting connections since UDP is a conectionlless protocol

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)