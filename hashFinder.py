#Author: Pablo Moles
#For more info read the README

import re
import urllib
import time

RED = '\033[91m'
ENDC = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

hashFile = open("hashes.txt","a")

while(1):
	try:
		web = urllib.urlopen("http://www.pastebin.com/realtime")
	except urllib.error.URLError as e:
		print RED, e.reason, ENDC
	webs = list(elem.split('/')[1] for elem in re.findall(r"\[<a href=\"/[a-zA-Z\d]{8}",web.read()))
	web.close()
	#print webs

	for url in webs:
		print BLUE, url, ENDC
		try:
			w = urllib.urlopen("http://www.pastebin.com/"+url)
		except urllib.error.URLError as e:
			print RED, e.reason, ENDC
		for hashFounded in re.findall(r"(?i)(?<![a-z0-9])[a-f0-9]{32,41}(?![a-z0-9]):[a-zA-Z\d][a-zA-Z\d]*", w.read()):
			hashFile.write(hashFounded + '\n')
			print GREEN, hashFounded, ENDC
	time.sleep(25)	
