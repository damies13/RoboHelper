#!/bin/python3

import signal
import os
import configparser
import argparse
import threading
import socket
import sys
import inspect

import time
from datetime import datetime

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer, HTTPServer
import uuid

from robot.api import TestSuite
from robot import run


# Local imports
# from rh_webserver import RH_WebServer
# from rh_webserver import *
import rh_webserver

class RoboHelper():
	version="0.0.1"
	debuglvl = 0

	rh_ini = None
	save_ini = True

	appstarted = False
	keeprunning = True

	def __init__(self):
		self.debugmsg(0, "Robo Helper")
		self.debugmsg(0, "	Version", self.version)
		signal.signal(signal.SIGINT, self.on_closing)
		signal.signal(signal.SIGHUP, self.on_closing)

		self.debugmsg(9, "ArgumentParser")
		# Check for command line args
		parser = argparse.ArgumentParser()
		parser.add_argument('-g', '--debug', help='Set debug level, default level is 0')
		parser.add_argument('-v', '--version', help='Display the version and exit', action='store_true')
		parser.add_argument('-i', '--ini', help='path to alternate ini file')
		parser.add_argument('-d', '--dir', help='Data directory')
		parser.add_argument('-e', '--ipaddress', help='IP Address to bind the server to')
		parser.add_argument('-p', '--port', help='Port number to bind the server to')
		self.args = parser.parse_args()

		if self.args.debug:
			self.debugmsg(9, "self.debuglvl: ", self.debuglvl)
			self.debugmsg(9, "self.args.debug: ", self.args.debug)
			self.debuglvl = int(self.args.debug)
			self.debugmsg(6, "self.debuglvl: ", self.debuglvl)

		self.debugmsg(5, "self.args: ", self.args)

		if self.args.version:
			exit()

		self.debugmsg(6, "ConfigParser")
		self.config = configparser.ConfigParser()
		scrdir = os.path.abspath(os.path.dirname(__file__))
		self.debugmsg(6, "scrdir: ", scrdir)

		self.rh_ini = os.path.join(scrdir, "RoboHelper.ini")
		if self.args.ini:
			self.save_ini = False
			self.debugmsg(5, "self.args.ini: ", self.args.ini)
			self.rh_ini = self.args.ini

		if os.path.isfile(self.rh_ini):
			self.debugmsg(9, "rh_ini: ", self.rh_ini)
			self.config.read(self.rh_ini)
		else:
			self.saveini()
		self.debugmsg(0, "Configuration File: ", self.rh_ini)


		if 'Server' not in self.config:
			self.config['Server'] = {}
			self.saveini()

		if 'BindIP' not in self.config['Server']:
			self.config['Server']['BindIP'] = ''
			self.saveini()

		if 'BindPort' not in self.config['Server']:
			self.config['Server']['BindPort'] = "8272" 		# ASCII R = 82, ASCII H = 72
			self.saveini()

		if 'DataDir' not in self.config['Server']:
			self.config['Server']['DataDir'] = scrdir
			self.saveini()

		if 'DBFile' not in self.config['Server']:
			self.config['Server']['DBFile'] = "TestDataTable.sqlite3"
			self.saveini()


		if 'Resources' not in self.config:
			self.config['Resources'] = {}
			self.saveini()

		if 'js_jquery' not in self.config['Resources']:
			self.config['Resources']['js_jquery'] = 'https://unpkg.com/jquery@latest/dist/jquery.min.js'
			self.saveini()

		if 'js_jqueryui' not in self.config['Resources']:
			self.config['Resources']['js_jqueryui'] = 'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js'
			self.saveini()

		if 'css_jqueryui' not in self.config['Resources']:
			self.config['Resources']['css_jqueryui'] = 'https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css'
			self.saveini()

		if 'js_papaparse' not in self.config['Resources']:
			self.config['Resources']['js_papaparse'] = 'https://unpkg.com/papaparse@latest/papaparse.min.js'
			self.saveini()


		if self.args.dir:
			self.save_ini = False
			self.debugmsg(5, "self.args.dir: ", self.args.dir)
			DataDir = os.path.abspath(self.args.dir)
			self.debugmsg(5, "DataDir: ", DataDir)
			self.config['Server']['DataDir'] = DataDir

		if self.args.ipaddress:
			self.save_ini = False
			self.debugmsg(5, "self.args.ipaddress: ", self.args.ipaddress)
			self.config['Server']['BindIP'] = self.args.ipaddress

		if self.args.port:
			self.save_ini = False
			self.debugmsg(5, "self.args.port: ", self.args.port)
			self.config['Server']['BindPort'] = self.args.port

		self.debugmsg(5, "run_web_server")
		self.webserver = threading.Thread(target=self.run_web_server)
		self.webserver.start()


		self.debugmsg(9, "__init__ ended")

	def mainloop(self):
		self.debugmsg(9, "mainloop started")
		self.debugmsg(7, " ")
		self.debugmsg(9, "appstarted:", self.appstarted)
		while not self.appstarted:
			self.debugmsg(9, "sleep(1)")
			time.sleep(1)
			self.debugmsg(9, "appstarted:", self.appstarted)

		self.debugmsg(9, "keeprunning:", self.keeprunning)
		i = 0
		while self.keeprunning:
			time.sleep(1)
			if i > 9:
				self.debugmsg(9, "keeprunning:", self.keeprunning)
				i = 0
			i +=1

		self.debugmsg(9, "mainloop ended")

	def on_closing(self, *args):
		self.debugmsg(9, "on_closing")

	def saveini(self):
		self.debugmsg(7, " ")
		if self.save_ini:
			with open(self.rh_ini, 'w') as configfile:    # save
			    self.config.write(configfile)

	def run_web_server(self):
		self.debugmsg(7, " ")

		srvip = self.config['Server']['BindIP']
		srvport = int(self.config['Server']['BindPort'])
		if len(srvip)>0:
			srvdisphost = srvip
			ip = ipaddress.ip_address(srvip)
			self.debugmsg(5, "ip.version:", ip.version)
			if ip.version == 6 and sys.version_info < (3, 8):
				self.debugmsg(0, "Python 3.8 or higher required to bind to IPv6 Addresses")
				pyver = "{}.{}.{}".format(sys.version_info[0], sys.version_info[1], sys.version_info[2])
				self.debugmsg(0, "Python Version:",pyver,"	IP Version:", ip.version, "	IP Address:", srvip)
				srvip = ''
				srvdisphost = socket.gethostname()
		else:
			srvdisphost = socket.gethostname()


		self.http_server_address = (srvip, srvport)
		try:
			self.appstarted = True
			self.webserver_functions = rh_webserver.RH_WebServer_Functions(self)
			self.httpserver = ThreadingHTTPServer(self.http_server_address, RH_WebServer)
		except PermissionError:
			self.debugmsg(0, "Permission denied when trying :",self.http_server_address)
			self.on_closing()
			return False
		except Exception as e:
			self.debugmsg(5, "e:", e)
			self.on_closing()
			return False

		# self.httpserver.set_core(self)

		self.appstarted = True
		self.debugmsg(5, "appstarted:", self.appstarted)
		serverurl = "http://{}:{}/".format(srvdisphost, srvport)
		serverlink = self.console_link(serverurl)
		self.debugmsg(0, "Starting Robo Helper Server", serverlink)
		self.httpserver.serve_forever()
		self.httpservercore.httpserver.serve_forever()

	def debugmsg(self, lvl, *msg):
		msglst = []
		prefix = ""

		# print("debugmsg: debuglvl:", self.debuglvl," >= lvl:",lvl,"	msg:", msg)

		if self.debuglvl >= lvl:
			try:
				if self.debuglvl >= 4:
					stack = inspect.stack()
					the_class = stack[1][0].f_locals["self"].__class__.__name__
					the_method = stack[1][0].f_code.co_name
					the_line = stack[1][0].f_lineno
					# print("RFSwarmBase: debugmsg: I was called by {}.{}()".format(str(the_class), the_method))
					prefix = "{} | {}: {}({}): [{}:{}]	".format(datetime.now().isoformat(sep=' ',timespec='seconds'), str(the_class), the_method, the_line, self.debuglvl, lvl)
					# <36 + 1 tab
					# if len(prefix.strip())<36:
					# 	prefix = "{}	".format(prefix)
					# <32 + 1 tab
					if len(prefix.strip())<32:
						prefix = "{}	".format(prefix)
					# <28 + 1 tab
					# if len(prefix.strip())<28:
					# 	prefix = "{}	".format(prefix)
					# <24 + 1 tab
					if len(prefix.strip())<24:
						prefix = "{}	".format(prefix)

					msglst.append(str(prefix))

				for itm in msg:
					msglst.append(str(itm))
				print(" ".join(msglst), flush = True)
			except Exception as e:
				# print("debugmsg: Exception:", e)
				pass

	def console_link(self, uri, label=None):
	    if label is None:
	        label = uri
	    parameters = ''

	    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
	    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

	    return escape_mask.format(parameters, uri, label)

	def get_tasks(self):

		suite = TestSuite.from_file_system('HackXIt.robot')

		for test in suite.tests._items:
			test.name

	def run_on_tag(self):

		# run('HackXIt.robot', include=['first'])
		run('.', include=['first'], variable=['LIST_BOOL:[True, True, True]'])


class RH_WebServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		core.debugmsg(5, "do_HEAD")
		self.process_response(core.webserver_functions.head(self))
		return

	def do_DELETE(self):
		core.debugmsg(5, "do_DELETE")
		self.process_response(core.webserver_functions.delete(self))
		return

	def do_PUT(self):
		core.debugmsg(5, "do_PUT")
		self.process_response(core.webserver_functions.put(self))
		return

	def do_POST(self):
		core.debugmsg(5, "do_POST")
		self.process_response(core.webserver_functions.post(self))
		return

	def do_GET(self):
		core.debugmsg(5, "do_GET")
		self.process_response(core.webserver_functions.get(self))
		return

	def process_response(self, objResp):

		core.debugmsg(5, "objResp:", objResp)
		core.debugmsg(5, "objResp.httpcode:", objResp.httpcode)
		core.debugmsg(5, "objResp.headers:", objResp.headers)
		core.debugmsg(5, "objResp.message:", objResp.message)

		self.send_response(objResp.httpcode)
		for header in objResp.headers:
			self.send_header(header[0], header[1])
		self.end_headers()
		if objResp.message is not None:
			self.wfile.write(bytes(objResp.message, "utf-8"))

	# 	log_request is here to stop BaseHTTPRequestHandler logging to the console
	# 		https://stackoverflow.com/questions/10651052/how-to-quiet-simplehttpserver/10651257#10651257
	def log_request(self, code='-', size='-'):
		core.debugmsg(9, "code:", code, "	size:", size, self)


if __name__ == "__main__":
	core = RoboHelper()
	core.debugmsg(0, "core:", core)
	try:
		core.debugmsg(0, "Run mainloop")
		core.mainloop()
	except KeyboardInterrupt:
		core.on_closing()
	except Exception as e:
		core.debugmsg(0, "self.Exception:", e)
		core.on_closing()

#
