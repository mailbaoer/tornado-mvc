'''
Created on Mar 4, 2014

@author: root

convert object to dict,so that it can be formated as json
'''

class JsonUtil:
    def __init__(self):
        pass
    def pingExportToJson(self,fromData):
        toData = []
        for items in fromData:
            ss = {}
            ss['IP']=items.getIp()
            ss['send']=items.getSend()
            ss['received']=items.getReceived()
            ss['lose']=items.getLose()
            ss['min']=items.getMin()
            ss['avg']=items.getAvg() 
            ss['max']=items.getMax()
            toData.append(ss) 
        return toData
    
    def httpExportToJson(self,fromData):
        toData = []
        for items in fromData:
            ss = {}
            ss['IP']=items.getIp()
            ss['code']=items.getCode()
            ss['connTime']=items.getConnTime()
            ss['preTran']=items.getPreTran()
            ss['startTran']=items.getStartTran()
            ss['totalTime']=items.getTotalTime() 
            ss['size']=items.getSize()
            toData.append(ss) 
        return toData
        