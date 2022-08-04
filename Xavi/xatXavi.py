from xml.etree import ElementTree
from json import dumps, loads
import requests

class login:
	def __init__(self):
		self.userConfig = {
			'id': 1533163695
		}

		self.buildXavi(self.readData())

	def buildXavi(self, y):
		try:
			buildXavi = {
				'head': {
					'id': 0,	'y': 0,	'sx': 15,
					'sy': 15,	'r': 180,	'color': '#E30B5C'
				},
				'mouth': {
					'id': 2,	'x': 0,		'y': 3,
					'sx': 15,	'sy': 15,	'r': 180,
					'color': '#E30B5C'
				},
				'eyes': { 
					'id': 0,	'x': 5,		'y': 0,
					'sx': 5,	'sy': 5,	'r': 0,
					'color': '#E30B5C'
				},
				'brows': {
					'id': 1,	'x': 3,		'y': -3,
					'sx': 0,	'sy': 0,	'r': 0,
					'color': '#000000'
				},
				'hair': {
					'id': 0,	'x': 0,		'y': 0,
					'sx': 0,	'sy': 0,	'r': 0,
					'color': '#FFFFFF'
				},
				'items': {
					'id': 0,	'x': 0,		'y': 0,
					'sx': 5,	'sy': 5,	'r': 999,
					'color': '#000000'
				}
			}

			buildXavi = dumps(buildXavi)

			headers = {
				'User-Agent': 	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Origin': 		'https://xat.com'
			}

			data = {
				"u": 	str(self.userConfig['id']),
				"au": 	None,
				"j": 	None,
				"v": 	None,
				"i": 	y['i'], #y['i']
				"k": 	y['k'], #y['k']
				"s": 	y['s'], #y['s']
				"t": 	y['t'], #y['t']
				"xavi": buildXavi
			}

			sendPost = requests.post('https://xat.com/json/xavi2/put.php', headers = headers, data = data, timeout = 5)
			status = sendPost.text

			if sendPost.status_code == 200:
				print('[Recv][xat]', sendPost)

			print('[Recv][xat]', status)

		except (Exception) as e:
			print(e)

	def readData(self):
		logData = open("xavi.txt", 'r').read()
		data = self.xmlArray(logData)

		print('[Load][xat]', logData)
		
		return data

	def chatID(self, chat):
		Chat = requests.get("http://xat.com/web_gear/chat/roomid.php?d=" + str(chat))
		Chat = Chat.json()
		return Chat['id']

	def xmlArray(self, xml):
		try:
			_return = {}
			array = ElementTree.fromstring(xml if xml[-1:] != chr(0) else xml[:-1])
			_return[chr(0)] = array.tag
			for i in array.attrib:
				_return[i] = array.attrib[i]
		finally: return _return

login()