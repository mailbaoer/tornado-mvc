'''
Created on Feb 28, 2014

@author: root

use to implements http healthcheck db operation

'''
import motor
import tornado.gen
from com.tornadoweb.demo.module import HttpHealth
from com.tornadoweb.demo.dao import BaseDao
class HttpDao(BaseDao.baseDao):
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
            pp = HttpHealth.HttpHealth()
            pp.setIp(items['IP'])
            pp.setCode(items['code'])
            pp.setConnTime(items['connTime'])
            pp.setPreTran(items['preTran'])
            pp.setStartTran(items['startTran'])
            pp.setTotalTime(items['totalTime'])
            pp.setSize(items['size'])
            
            selectResult.append(pp)
        return selectResult
        
        