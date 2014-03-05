'''
Created on Mar 3, 2014

@author: root
'''
import tornado.gen
import tornado.web
import json
from com.tornadoweb.demo.service import HttpService
from com.tornadoweb.demo.util import JsonUtil
class HttpHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        newservice = HttpService.HttpService()
        nums = int(self.get_argument('id'))
        result = yield newservice.selectservice(nums)
        #print (result)
        result = JsonUtil.JsonUtil.httpExportToJson(self,result)
        self.write(json.dumps(result))
        self.set_header("Content-Type","application/json;charset=utf-8")