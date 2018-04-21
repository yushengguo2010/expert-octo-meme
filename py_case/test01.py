import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run on the given port', type=int)
define('version', default=0.01, help='show the version', type=str)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_argument('name', 'no')
		self.write(name)

		name = self.get_arguments('name')
		self.flush()
		self.write('<br>')
		self.write(','.join(name)+' , nice to meet you!')

class HtmlHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("in_out.html")

class RecHandler(tornado.web.RequestHandler):
	def get(self):
		import time
		time.sleep(3)
		self.redirect(r'/h')

class ReqHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(self.request.remote_ip)
		print(type(self.request.remote_ip), repr(self.request.remote_ip))
		print(self.request.full_url())
		print(self.request.request_time())


application = tornado.web.Application(
	handlers=[
		(r"/test", IndexHandler),
		(r"/h", HtmlHandler),
		(r"/rec", RecHandler),
		(r"/req", ReqHandler),

	],
	template_path='templates',
	debug=True
)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
