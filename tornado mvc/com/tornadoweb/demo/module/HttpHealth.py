'''
Created on Mar 3, 2014

@author: root
'''
class HttpHealth():
    IP = '192.168.1.1'
    code = '15'
    connTime = '15'
    preTran = '100%'
    startTran = '0'
    totalTime = '0'
    size = '0'
    def __init__(self):
        pass
    def setIp(self,IP):
        self.IP = IP
    def getIp(self):
        return self.IP
    def setCode(self,code):
        self.code = code
    def getCode(self):
        return self.code
    def setConnTime(self,connTime):
        self.connTime = connTime
    def getConnTime(self):
        return self.connTime
    def setPreTran(self,preTran):
        self.preTran = preTran
    def getPreTran(self):
        return self.preTran
    def setStartTran(self,startTran):
        self.startTran =startTran
    def getStartTran(self):
        return self.startTran
    def setTotalTime(self,totalTime):
        self.totalTime = totalTime
    def getTotalTime(self):
        return self.totalTime
    def setSize(self,size):
        self.size = size
    def getSize(self):
        return self.size
    
        