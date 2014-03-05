'''
Created on Mar 3, 2014

@author: root
'''
import tornado.gen
import tornado.web
import json
from com.tornadoweb.demo.service import PingService
from com.tornadoweb.demo.util import JsonUtil
class PingHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        newservice = PingService.PingService()
        nums = int(self.get_argument('id'))
        result = yield newservice.selectservice(nums)
        #print (result)
        result = JsonUtil.JsonUtil.pingExportToJson(self,result)
        self.write(json.dumps(result))
        self.set_header("Content-Type","application/json;charset=utf-8")