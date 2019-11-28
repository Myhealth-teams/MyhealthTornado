import datetime
import os
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define,options
from tornado.websocket import WebSocketHandler
# from tornado.ioloop import IOLoop

define("port", default=8000, type=int)




class ChatHandler(WebSocketHandler):
    users = set() # 用户ID
    client_id = 1
    def open(self):

         # 每个用户独有的ID
        ChatHandler.client_id +=1
        self.client_id = ChatHandler.client_id
        self.users.add(self)
        # for u in self.users:  #登录告知所有人
        #     data = {
        #         "user":self.client_id,
        #         "time":datetime.datetime.now().strftime("%H:%M:%S"),
        #         "state":"1"
        #     }
        #     u.write_message(data)
        # print(self.client_id,"连接成功")

    def on_message(self, message):
        print(self.client_id,"正在发消息")
        for u in self.users: # 向在在线用户广播消息
            if u != self:
                data = {
                    "user": self.client_id,
                    "time": datetime.datetime.now().strftime("%H:%M:%S"),
                    "state":"发消息",
                    "msg":message
                }
                u.write_message(data)


    def on_close(self):
        print(self.client_id,"退出聊天室")
        self.users.remove(self)
        # for u in self.users:
        #     data = {
        #         "user": self.client_id,
        #         "time": datetime.datetime.now().strftime("%H:%M:%S"),
        #         "state": "0",
        #     }
        #     u.write_message(data)

    def check_origin(self, origin):
        return True

settings = {
        "static_path" : os.path.join(os.getcwd(), "static"),    #ico文件路径
        "template_path" : os.path.join("templates"), #视图文件路径
        "cookie_secret" : "DONT_SHOW_SECRET",
        "xsrf_cookies" :True,  #预防跨站攻击
         "debug":True
}

def make_app():
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/chat/", ChatHandler),
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    application = tornado.ioloop.IOLoop.current()
    return application

application = make_app()
if __name__ == '__main__':
    # tornado.options.parse_command_line()
    # app = tornado.web.Application([
    #         (r"/chat/", ChatHandler),
    #     ],**settings)
    #
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(options.port)
    application.start()
