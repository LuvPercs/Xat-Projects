from random import random, randint, choice
from xml.etree import ElementTree
from json import dumps, loads
from threading import Thread
from time import sleep, time
from select import select
from lxml import etree
from socket import *
import requests

class login:
	def __init__(self):
		self.userConfig = {
			'id': '0',
			'reg': 'regname_here',
			'pw': '$crc32_here'
		}

		print('[Send]', dumps(self.userConfig))

		self.connectToXat()

		sleep(50)
		
	def connectToXat(self):
		self.Xat = socket(AF_INET, SOCK_STREAM, SOL_TCP)
		self.Xat.connect(('fwdelb01-1365137239.us-east-1.elb.amazonaws.com', 80))

		self.Xat.send(bytes('<y r="8" v="0" u="42" />\0', encoding='utf-8'))
		print('[Recv]', self.Xat.recv(4068).decode('utf-8', 'ignore'))

		self.Xat.send(bytes('<v n="%s" p="%s" />\0' % (str(self.userConfig['reg']), str(self.userConfig['pw'])), encoding='utf-8'))
		print('[Recv]', self.Xat.recv(4068).decode('utf-8', 'ignore'))

	def xmlArray(self, xml):
		try:
			_return = {}
			array = ElementTree.fromstring(xml if xml[-1:] != chr(0) else xml[:-1])
			_return[chr(0)] = array.tag
			for i in array.attrib:
				_return[i] = array.attrib[i]
		finally: return _return

login()