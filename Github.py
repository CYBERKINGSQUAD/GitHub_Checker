#!/usr/bin/env python
# : Rh077king
# GitHub Take over 69

import re, sys,os
from datetime import datetime
import requests
from Queue import Queue
from threading import Thread
from urlnorm import norm as urlnorm
from random import sample as rand
requests.packages.urllib3.disable_warnings()
from colorama import Fore,init

init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
b = Fore.RED
w = Fore.GREEN
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
banner = """
{}

 ##################################################################
 ##{}{}{}             Github Takeover Scanner                          ##
 ##{}{}{}        Author  :    Rh077king                                ##
 ##{}{}{}        Facebook:    https://www.facebook.com/Rh077King       ##
 ##{}{}{}        Telegram:    https://t.me/Rh077king                   ##
 ##################################################################
   
"""

print(banner.format(g,b,g,w,r,b,g,r,g,r,g,r,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g))

def exploit (url) :





	res      = requests.get (url, verify = False,timeout=2)

	if res.status_code==404:
		open ('Vulnerable.txt', 'a').write (url + '\n')
		return True

	return False

def start_worker () :
	while True :
		try :
			url = urlnorm (q.get ())

			if exploit (url) :
				sys.stdout.write (url + ' \033[1;31;42m ===> Vulnerable \033[0;0m \n')
			else :
				sys.stdout.write (url + ' \033[1;31;43m ===> Not Vulnerable \033[0;0m \n')
		except :
			pass

		q.task_done ()

NUMBER_OF_THREADS =  3
q = Queue ()

# start threads
for i in range (NUMBER_OF_THREADS) :
	t = Thread (target = start_worker)
	t.daemon = True
	t.start ()

if len (sys.argv) > 1 :
	try :
		file = open (sys.argv[1])
	except IOError :
		print 'File Not Found'
		exit (-1)

	for url in file :
	  if 'http://' not in url:
                url='http://'+url
		q.put (url.strip ())

	q.join () # block until all threads are done
else :
	print '\n\tUsage: python2 ' + sys.argv[0] + ' list.txt'
