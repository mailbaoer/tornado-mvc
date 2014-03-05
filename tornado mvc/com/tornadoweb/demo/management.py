'''
Created on Mar 3, 2014

@author: root
'''
import tornado.web
import tornado.ioloop
from com.tornadoweb.demo.handler import PingHandler
from com.tornadoweb.demo.handler import HttpHandler
from com.tornadoweb.demo.util import checkhandler
if __name__ == '__main__':
    application = tornado.web.Application([
                                           (r'/API/gslb/ping.do',PingHandler.PingHandler),
                                           (r'/API/gslb/http.do',HttpHandler.HttpHandler),
                                           ])
    application.listen(8888)

    tornado.ioloop.PeriodicCallback(checkhandler.ping_handler,15000).start()
    tornado.ioloop.PeriodicCallback(checkhandler.http_handler,15000).start()
    tornado.ioloop.IOLoop.instance().start()
    