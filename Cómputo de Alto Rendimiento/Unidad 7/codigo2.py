from threading import Thread
import os, re, time, sys

class testit(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1
        
    def run(self):
        pingalign = os.popen("ping -q -c2 " + self.ip, "r")
        while 1:
            line = pingalign.readline()
            if not line: break
            igot = re.findall(testit.lifeline, line)
            if igot:
                self.status = int(igot[0])

testit.lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

print (time.ctime())
pinglist = [ ]
for host in range(40,50):
    ip = "192.168.135."+str(host)
    current = testit(ip)
    pinglist.append(current)
    current.start()
for pingle in pinglist:
    pingle.join()
    print ("Status from ",pingle.ip,"is",report[pingle.status])
    
print(time.ctime())