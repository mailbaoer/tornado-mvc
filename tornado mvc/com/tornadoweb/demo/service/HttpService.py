'''
Created on Mar 3, 2014

@author: root


'''
import tornado.gen
from com.tornadoweb.demo.dao import HttpDao
from com.tornadoweb.demo.config import appconf
class HttpService:
    @tornado.gen.coroutine
    def selectservice(self,nums):
        dao = HttpDao.HttpDao()
        dao.getConnection(appconf.dbIP, int(appconf.dbPort))
        db = dao.getDatabase(appconf.database)
        collection = dao.getCollection(appconf.http_collection)
        result = []
        result = yield dao.baseSelect(collection, {'IP':'10.19.95.90'}, nums)
        return result
        