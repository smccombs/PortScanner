import socket
import sys

tgthost = sys.argv[1]
scantype = sys.argv[2]
tgtport1 = sys.argv[3]

socket.gethostbyname(tgthost)
socket.setdefaulttimeout(1.1)
connectionsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if scantype == 'range':
	tgtport2 = sys.argv[4]
	tgtport1 = int(tgtport1)
	tgtport2 = int(tgtport2)
	for port in range(tgtport1, tgtport2+1):
		try:
			connectionsocket.connect((tgthost, port))
			print "%s:%d --port open" %(tgthost, port)
			connectionsocket.close()
		except:
			print "%s:%d --port closed" %(tgthost, port)
elif scantype == 'list':
	tgtports = tgtport1.split(',')
	for port in tgtports:
		port = int(port)
		try:
			connectionsocket.connect((tgthost, port))
			print "%s:%d --port open" %(tgthost, port)
			connectionsocket.close()
		except:
			print "%s:%d --port closed" %(tgthost, port)