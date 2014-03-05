'''
Created on Mar 3, 2014

@author: root
'''
import tornado.gen
from com.tornadoweb.demo.dao import PingDao
from com.tornadoweb.demo.config import appconf
from com.tornadoweb.demo.config import appconf 
class PingService:
    @tornado.gen.coroutine
    def selectservice(self,nums):
        dao = PingDao.PingDao()
        dao.getConnection(appconf.dbIP, int(appconf.dbPort))
        db = dao.getDatabase(appconf.database)
        collection = dao.getCollection(appconf.ping_collection)
        result = []
        result = yield dao.baseSelect(collection, {'IP':'192.168.191.102'}, nums)
        return result
    def insertService(self):
        dao = PingDao.PingDao()
        dao.getConnection(appconf.dbIP, int(appconf.dbPort))
        db = dao.getDatabase(appconf.database)
        collection = dao.getCollection(ping_collection)
        