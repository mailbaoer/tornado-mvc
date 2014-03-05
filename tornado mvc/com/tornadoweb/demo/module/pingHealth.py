'''
Created on Mar 3, 2014

@author: root
'''
class pingHealth():
    IP = '192.168.1.1'
    send = '15'
    received = '15'
    lose = '100%'
    min = '0'
    avg = '0'
    max = '0'
    params = ['IP','send','received','lose','min','avg','max']
    def __init__(self):
        pass
    def setIp(self,IP):
        self.IP = IP
    def getIp(self):
        return self.IP
    def setSend(self,send):
        self.send = send
    def getSend(self):
        return self.send
    def setReceived(self,received):
        self.received = received
    def getReceived(self):
        return self.received
    def setLose(self,lose):
        self.lose = lose
    def getLose(self):
        return self.lose
    def setMin(self,min):
        self.min =min
    def getMin(self):
        return self.min
    def setAvg(self,avg):
        self.avg = avg
    def getAvg(self):
        return self.avg
    def setMax(self,max):
        self.max = max
    def getMax(self):
        return self.max
    
        