import subprocess
import ipgetter
import time
import sys

from twitter import *
from datetime import datetime


#consts
DEFAULT_IP = "8.8.8.8"  #Google primary DNS google-public-dns-a.google.com
DEFAULT_DELAY = 2

#tw tokkens
TW_API_KEY = ""
TW_API_SEC = ""
TW_ACC_TOK = ""
TW_ACC_SEC = ""

address = DEFAULT_IP
delay = DEFAULT_DELAY
ip = ipgetter.myip()

#getting ip
if(len(sys.argv)>1):
	address = sys.argv[1]
#getting delay
if(len(sys.argv)>1):
	delay = int(sys.argv[2])

print(sys.argv)

def parseTime(dt):
	return dt.strftime("%I:%M%:%S%p")

def sendTweet(address=address, now=parseTime(datetime.now()), ip=ip):
	t = Twitter(auth=OAuth(TW_ACC_TOK, TW_ACC_SEC, TW_API_KEY, TW_API_SEC))
	msg = "No hay respuesta de ping a las "+str(now)+" @NetlifeEcuador @jegerima. Interval: "+str(delay)+"s, Test: "+str(address)+", PublicIP: "+str(ip)
	print(len(msg),"Sending tweet to timeline:", msg)
	t.statuses.update(status=msg)

while(True):
	res = subprocess.call(['ping','-c', '1', address], stdout=subprocess.PIPE)
	now = parseTime(datetime.now());
	if(res == 0):
		print("ping to", address, "OK", now, "public:", ip)
		ip = ipgetter.myip()
		#sendTweet(address, now,ip)
	elif(res == 2):
		sendTweet(address, now, ip)
		print("no response from", address)
	else:
		sendTweet(address, now, ip)
		print("ping to", address, "failed!")

	time.sleep(delay)


#https://stackoverflow.com/questions/12101239/multiple-ping-script-in-python
#https://stackoverflow.com/questions/4996852/how-to-just-call-a-command-and-not-get-its-output

#pip3 install ipgetter
#pip3 install twitter
#https://github.com/sixohsix/twitter/tree/master
