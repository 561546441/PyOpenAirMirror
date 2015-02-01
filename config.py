model = "OpenAirMirror0,1"

server_name = "AirTunes"
server_version = "150.33"
service_name = "OpenAirMirror"
sdl_window_caption = service_name

selectedSinks = []
password = None

default_capabilities = {
		"width": 1280,
		"height": 720,
		"overscanned": True,
		"version": server_version,
		"refreshRate": 1.0/60,
}

fplyServerPort = 20992
fplyServer = None

#####################################################################

import argparse
import FrameSink

args = None

def parseArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("name", type=str, nargs='?',
			            help="the name under which the service gets announced",
						default=service_name)
	parser.add_argument("--sink", "-s", nargs='+',
						choices=FrameSink.availableSinks.keys(),
						default=["sdl"],
						help="What to do with received frames")
	parser.add_argument("--password", "-p",
						help="server's password (none if not provided)")
	parser.add_argument("--fply-server", "-f", type=str,
						help="a server that can answer FPLY challenges")

	global args
	args = parser.parse_args()
	applyArguments()

def applyArguments():
	global service_name
	global password
	global selectedSinks
	global fplyServer, fplyServerPort
	service_name = args.name
	password = args.password
	selectedSinks = [FrameSink.availableSinks[key] for key in args.sink]
	fplyServer = args.fply_server
	if fplyServer is not None and ':' in fplyServer:
		fplyServer, _, fsp = fplyServer.rpartition(':')
		fplyServerPort = int(fsp)

