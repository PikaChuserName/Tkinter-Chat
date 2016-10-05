import thread
import time
import sys
from socket import *

def func1():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(('0.0.0.0',2085))
    s.listen(1)
    con, addr = s.accept()
    while 1:
        try:    
            data = con.recv(1024)
            print data
        except:     
            con.close()
            s.close()
            sys.exit(1)

def func2():
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(('192.168.134.1',2085))
    while 1:
        s.sendall(raw_input())             

def main():
    thread.start_new_thread(func1, ())
    time.sleep(1)
    func2()

if __name__== "__main__":
    main()
