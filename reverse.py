import socket

# declaration of the socket
# see documentation
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to the server
ipaddress = ""
sock.connect((ipaddress, 54321))
print("Connection established to the server")


# close the socket
sock.close()