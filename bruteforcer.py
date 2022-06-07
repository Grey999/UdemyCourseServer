import threading
import sys
import requests
import getopt

class Bruteforcer:
    global banner

    def print_banner(self):
        print("##############################")
        print("*  Bruteforcer by Thanatos   *")
        print("##############################")


    def launcher_thread(self, passwords, threads, user, url):
        global list
        list = []


    def start(self, argv):
        self.print_banner()
        try:
            opts, args = getopt.getopt(argv, "u:w:f:t")
        except getopt.GetoptError:
            print("Error on arguments")
            sys.exit()
        for opt,arg in opts:
            if opt == "-u":
                user = arg
            elif opt == "-w":
                url = arg
            elif opt == "-f":
                passlist = arg
            elif opt == "-t":
                threads = arg
        try:
            f = open(passlist, "r")
            passwords = f.readlines()
        except:
            print("[!!] Can't open the file !!")
            sys.exit()
        self.launcher_thread(passwords,threads, user, url)

    def main(self):
        if __name__ == "__main__":
            try:
                self.start(sys.argv)
            except KeyboardInterrupt:
                print("[!!]Interrupted")