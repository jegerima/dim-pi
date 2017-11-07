import subprocess
import time
import sys

from datetime import datetime

#consts
default_ip = "8.8.8.8"  #Google primary DNS google-public-dns-a.google.com
default_delay = 2

address = default_ip
delay = default_delay

#getting ip
if(len(sys.argv)>1):
	address = sys.argv[1]
#getting delay
if(len(sys.argv)>1):
	delay = int(sys.argv[2])

print(sys.argv)

def sendTweet(address):
	print("Sending tweet to timeline");

while(True):
	res = subprocess.call(['ping','-c', '1', address], stdout=subprocess.PIPE)
	if(res == 0):
		print("ping to", address, "OK", datetime.now())
	elif(res == 2):
		sendTweet(address)
		print("no response from", address)
	else:
		print("ping to", address, "failed!")

	time.sleep(delay)


#https://stackoverflow.com/questions/12101239/multiple-ping-script-in-python
#https://stackoverflow.com/questions/4996852/how-to-just-call-a-command-and-not-get-its-output
