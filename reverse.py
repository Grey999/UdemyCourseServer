import socket

# declaration of the socket
# see documentation
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to the server
ipaddress = ""
sock.connect((ipaddress, 54321))
print("Connection established to the server")

while True:
    message = sock.recv(1024)
    print(message)
    if message == "q":
        break
    else:
        answer = input("Type message to send to server: ")
        sock.send(answer)

# close the socket
sock.close()
