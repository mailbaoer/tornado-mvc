'''
Created on Feb 28, 2014

@author: root
'''
import motor
import tornado.gen
from com.tornadoweb.demo.module import pingHealth
from com.tornadoweb.demo.dao import BaseDao
class PingDao(BaseDao.baseDao):
    '''
    classdocs
    '''
    client = None
    database = None
    collection = None
    cursor = None
     
    @tornado.gen.coroutine
    def baseSelect(self,collection,conditions,limits=1):
        cursor = collection.find(conditions)
        selectResult = []
        for items in (yield cursor.to_list(length=limits)):
            pp = pingHealth.pingHealth()
            pp.setIp(items['IP'])
            pp.setSend(items['send'])
            pp.setReceived(items['received'])
            pp.setLose(items['lose'])
            pp.setMin(items['min'])
            pp.setAvg(items['avg'])
            pp.setMax(items['max'])
            selectResult.append(pp)
        return selectResult
    @tornado.gen.coroutine
    def ping_insert(self,collection,ping_health):
            yield collection.insert(ping_health)
                 
        