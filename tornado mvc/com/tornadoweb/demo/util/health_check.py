from io import StringIO
import platform
import pycurl
import os
import sys
import socket as sk
import http
from subprocess import Popen, PIPE
import re
from optparse import OptionParser
import threading
from threading import Thread
from queue import Queue
from com.tornadoweb.demo.config import appconf

NUM = 100
TIMEOUT=2
PORTS=[80]             
# convert an IP address from its dotted-quad format to its
# 32 binary digit representation


# convert a decimal number to binary representation
# if d is specified, left-pad the binary number with 0s to that length


def pinger():
    c = []
    global result 
    result = []
    while True:
        ip=q.get()
        if platform.system()=='Linux':
            p=Popen(['ping','-c 15 -i 1 -w 1',ip],stdout=PIPE)
            c.append(ip)
            for s in p.stdout.readlines():
                s = s.decode('UTF-8')
                m = re.search('(.*) packets transmitted, (.*) received, (.*)packet loss, time (.*)ms', s)
                if m != None:
                    c.append(m.group(1))
                    c.append(m.group(2))
                    c.append(m.group(3))
                m = re.search('= (.*)/(.*)/(.*)/(.*) ms', s)
                if m != None:
                    c.append(m.group(1))
                    c.append(m.group(2))
                    c.append(m.group(3))
                try:
                    if m.group(1)!='0':
                        pinglist.append(ip)
                except:pass
        if platform.system()=='Windows':
            p=Popen('ping -n 2 ' + ip, stdout=PIPE)
            m = re.search('TTL', p.stdout.read())
            if m:
                pinglist.append(ip)
        q.task_done()
        #print (c)
        result.append(c)


def scanipport():
    global lock
    global portResult
    portResult = []
    while True:
        host,port=sq.get()
        sd=sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        sd.settimeout(TIMEOUT)
        oneResult = []        
        try:
            sd.connect((host,port))
            lock.acquire()
            oneResult.append(host)
            oneResult.append(port)
            oneResult.append(1)
            lock.release()
            sd.close()
        except:
            oneResult.append(host)
            oneResult.append(port)
            oneResult.append(0)
        portResult.append(oneResult)
        sq.task_done()


 


def testping():
    global pinglist
    global q
    q=Queue()
    pinglist=[]
    for i in range(NUM):
        t = Thread(target=pinger)
        t.setDaemon(True)
        t.start()
    for ip in appconf.iplist:
        q.put(ip)
    q.join()
    return result

class Test:
        def __init__(self):
            self.contents = ''
        def body_callback(self,buf):
            self.contents = self.contents + buf.decode('utf-8')
 
def test_gzip(host):
        t = Test()
        global result
        result = []
        for ip in host:
            input_url = ''.join(host) + "/index.html"
            c = pycurl.Curl()
            c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
            c.setopt(pycurl.ENCODING, 'gzip')
            c.setopt(pycurl.URL,input_url)
            c.perform()
            http_code = c.getinfo(pycurl.HTTP_CODE)
            http_conn_time =  c.getinfo(pycurl.CONNECT_TIME)
            http_pre_tran =  c.getinfo(pycurl.PRETRANSFER_TIME)
            http_start_tran =  c.getinfo(pycurl.STARTTRANSFER_TIME)
            http_total_time = c.getinfo(pycurl.TOTAL_TIME)
            http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
            c = [] 
            c.append(ip)
            c.append(http_code)
            c.append(http_conn_time)
            c.append(http_pre_tran)
            c.append(http_start_tran)
            c.append(http_total_time)
            c.append(http_size)
            result.append(c)
def testservice():
    host = ['10.19.95.90']
    test_gzip(host)
    return result
def testport():
    print ("Scanning ports...\n")
    sq=Queue()
    lock = threading.Lock()
    for i in range(NUM):
        st = Thread(target=scanipport)
        st.setDaemon(True)
        st.start()    
    for scanip in iplist:
        for port in PORTS:            
            sq.put((scanip,port))
    sq.join()
    #print (portResult)
