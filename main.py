#!/usr/bin/env python

import threading
import BaseHTTPServer

import common.register

def runServer(port, handler):
	try:
		httpd = BaseHTTPServer.HTTPServer(('', port), handler)
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass

def main():
	register_thread = threading.Thread(target=common.register.registerAirPlay)
	register_thread.setDaemon(True)
	register_thread.start()

	import mirror.service
	runServer(7100, mirror.service.MirrorService)

if __name__ == "__main__":
	import config
	config.parseArguments()
	main()
