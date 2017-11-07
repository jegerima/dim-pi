import subprocess

for ping in range(1,255):
	address = "192.168.2." + str(ping)
	res = subprocess.call(['ping', '-c', '1', address])
	if(res == 0):
		print("ping to", address, "OK")
	elif(res == 2):
		print("no response from", address)
	else:
		print("ping to", address, "failed!")


#https://stackoverflow.com/questions/12101239/multiple-ping-script-in-python
