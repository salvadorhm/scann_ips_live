import socket
from datetime import datetime

ip= raw_input("Enter the IP address ")
ip1= net.split('.')
separator = '.'
ipf = ip1[0]+separator+ip1[1]+separator+ip1[2]+separator

st1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))

en1=en1+1
t1= datetime.now()

def scan(addr):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr,135))
    if result==0:
        return 1
    else :
        return 0

def run1():
    for ip in xrange(st1,en1):
        addr = net2+str(ip)
        if (scan(addr)):
            print addr , "is live"
run1()
t2= datetime.now()
total =t2-t1
print "scanning complete in " , total