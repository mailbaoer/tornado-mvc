'''
Created on Mar 5, 2014

@author: root

scheduled collect data insert into mongodb
'''
import motor
import tornado.ioloop
import tornado.web
import os
import com.tornadoweb.demo.util
import tornado.gen
import json
from com.tornadoweb.demo.util import health_check
from com.tornadoweb.demo.dao import PingDao
from com.tornadoweb.demo.dao import HttpDao
from com.tornadoweb.demo.config import appconf

#collect ping data

def ping_handler():
    dao = PingDao.PingDao()
    dao.getConnection(appconf.dbIP, int(appconf.dbPort))
    db = dao.getDatabase(appconf.database)
    collection = dao.getCollection(appconf.ping_collection)
    c = health_check.testping()
    for x in range(len(c)):
        #not None
        cc = {'IP':'192.168.1.1','send':'15','received':'15','lose':'100%','min':'0','avg':'0','max':'0'}
        try:
            cc['IP'] = c[x][0]
            cc['send'] = c[x][1]
            cc['received'] = c[x][2]
            cc['lose'] = c[x][3]
            cc['min'] = c[x][4]
            cc['avg'] = c[x][5]
            cc['max'] = c[x][6]
        except:
            pass
        collection.insert(cc)

# collect http service data

def http_handler():
    dao = HttpDao.HttpDao()
    dao.getConnection(appconf.dbIP, int(appconf.dbPort))
    db = dao.getDatabase(appconf.database)
    collection = dao.getCollection(appconf.http_collection)
    c = health_check.testservice()
    for x in range(len(c)):
        #not None
        cc = {'IP':'192.168.1.1','code':'0','connTime':'0','preTran':'0','startTran':'0','totalTime':'0','size':'0'}
        try:
            cc['IP'] = c[x][0]
            cc['code'] = c[x][1]
            cc['connTime'] = c[x][2]
            cc['preTran'] = c[x][3]
            cc['startTran'] = c[x][4]
            cc['totalTime'] = c[x][5]
            cc['size'] = c[x][6]
        except:
            pass
        collection.insert(cc)