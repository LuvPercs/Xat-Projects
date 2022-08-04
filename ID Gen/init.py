'''
	Title: Xat Multi-Threaded ID Generator
	Author: Armin [Perc (40302)]
	Date: /
	Description: Generates Xat IDs unbelievably fast.
'''

from threading import Thread
from requests import get
from time import sleep
from os import system
import random
import sys

sys.stderr = ''

system('title Multi-Threaded ID Generator')
print('/* Written by LuvPercs @github/LuvPercs */\n')

class xtGen:
	def __init__(self, Proxy, Prox):
		while True:
			# Proxies use User:Pass authentication.
			Proxy = Proxy.split(':')

			genData = {
				0: {
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
					'Content-Type': 'text/html'
				},
				1: {'https': str(Proxy[2]) + ':' + str(Proxy[3]) + '@' + str(Proxy[0]) + ':' + str(Proxy[1])},
				2: ['https://xat.com/web_gear/chat/auser3.php']
			}

			ID = get(genData[2][0], headers = genData[0], proxies = genData[1]).text

			self.filterID(ID)

	def filterID(self, data):
		if not data: return print('No data provided.')

		# Filters cloudflare page and false IDs/already used proxy.
		filter = ['<body>', '&k2=0', '\n']

		if data in filter:
			pass
		else:
			log = open('_inc/IDs.txt', 'a')
			log.write(f"{data}\n")
			log.close()

Proxies, Proxy = open('_inc/Proxies.txt', 'r').read().split('\n'), open('_inc/Proxies.txt', 'r').read().split('\n')

ActiveThreads = []
[ActiveThreads.append(Thread(target = xtGen, args = [Proxy, Prox])) for Proxy, Prox in zip(Proxies, Proxy)]

for tH in ActiveThreads: tH.start()	

xtGen()
