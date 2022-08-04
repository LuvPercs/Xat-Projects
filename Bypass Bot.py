'''
	Title: Xat Bypass Bot
	Author: Armin [Perc (40302)]
	Date: /
	Description: Minimal bypass bot for xat, no commands, just structure.
'''

from random import randint, choice
from xml.etree import ElementTree
from json import dumps, loads
from time import sleep, time
from threading import Thread
from select import select
from requests import get
from socket import *

class bypassBot:
	botConfig = {
		0: 1545040188,				# ID
		1: 'ede4d04f9862ec147400',	# K1
		2: 'Name',					# Name
		3: 5,						# Avatar
		4: 'Dev'					# Room
	}

	liveIP 	= get('https://xat.com/web_gear/chat/ip3.php').json()
	liveIP 	= liveIP['E1'][1][0].split(':')

	def __init__(self):
		print('[Connect]', '{}:{}\n'.format(str(self.liveIP[0]), str(self.liveIP[1])))
		
		self.createConnection()

	def createConnection(self):
		xat = socket(AF_INET, SOCK_STREAM, SOL_TCP)
		xat.connect((str(self.liveIP[0]), int(self.liveIP[1])))

		xat.send(self.build('y', [['r', str(self.chat(self.botConfig[4]))], ['v', '0'], ['u', str(self.botConfig[0])]]))
		xatAttr = self.xmlArray(xat.recv(4068).decode('utf-8', 'ignore'))

		xat.send(self.buildJ2(xatAttr['c'], xatAttr['i']))
		Data = self.xmlArray(xat.recv(4068).decode('utf-8', 'ignore'))

		while xat:
			recv = self.xmlArray(xat.recv(4068).decode('utf-8', 'ignore'))

			try:
				if recv:
					print('[Recv] ->', recv)
			except:
				pass

	def build(self, tag, _dict):
		return bytes('<' + tag + ' ' + (' '.join([_list[0] + '="' + _list[1] + '"' for _list in _dict])) + ' />\0', encoding = 'utf-8')

	def buildJ2(self, c, y):
		j2 = [
			['cb', str(c)],
			['Y', '2'],
			['l5', 'per'],
			['l4', str(randint(100, 200))],
			['l3', str(randint(100, 200))],
			['l2', '0'],
			['y', str(y)],
			['k', str(self.botConfig[1])],
			['k3', '0'],
			['z', 'm1.59,3'],
			['p', '300'],
			['c', str(self.chat(self.botConfig[4]))],
			['f', '2'],
			['u', str(self.botConfig[0])],
			['n', str(self.botConfig[2])],
			['a', str(self.botConfig[3])],
			['h', ''],
			['v', '1']
		]

		return self.build('j2', j2)

	def xmlArray(self, xml):
		try:
			_return = {}
			array = ElementTree.fromstring(xml if xml[-1:] != chr(0) else xml[:-1])
			_return['tag'] = array.tag
			for i in array.attrib:
				_return[i] = array.attrib[i]
		finally: return _return

	def chat(self, chat):
		Chat = get('http://xat.com/web_gear/chat/roomid.php?d={}'.format(str(chat))).json()
		return Chat['id']

bypassBot()
