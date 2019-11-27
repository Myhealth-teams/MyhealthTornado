import os

from tornado import httpserver, ioloop
from tornado.web import RequestHandler, url, Application
from tornado.options import define,options





define("port", default=6000, type=int)
class IndexHandler(RequestHandler):
    def get(self):
        self.render("index1.html")
class IndexHandler2(RequestHandler):
    def get(self):
        self.render("index.html")


settings = {
        "static_path" : os.path.join(os.getcwd(), "static"),    #ico文件路径
        "template_path" : os.path.join("templates"), #视图文件路径
        "cookie_secret" : "DONT_SHOW_SECRET",
        "xsrf_cookies" :True,  #预防跨站攻击
         "debug":True
}
if __name__ == '__main__':
    options.parse_command_line()
    app =Application([
            url(r"/index/",IndexHandler),
            url(r'/index1/',IndexHandler2)
        ],**settings)

    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.current().start()