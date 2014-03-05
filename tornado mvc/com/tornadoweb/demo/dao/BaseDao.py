'''
Created on Feb 28, 2014

@author: root
'''
import motor
import tornado.gen
class baseDao:
    '''
    classdocs
    '''
    client = None
    database = None
    collection = None
    cursor = None
     
        
    def getConnection(self,host,port):
        self.client = motor.MotorClient(host,port)
        return self.client
    
    def getDatabase(self,database):
        self.database =  self.client[database]
        return self.database
    
    def getCollection(self,collection):
        self.collection = self.database[collection]
        return self.collection
    @tornado.gen.coroutine
    def baseSelect(self,collection,conditions,limits=1):
        pass
        
        