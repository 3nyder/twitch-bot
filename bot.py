class Bot:
	#Future bot configs to import???
	def __init__(self, chat, channel):
		self.chat = chat
		self.channel = channel

	def send(self,message):
		self.chat.send("PRIVMSG {} :{}\r\n".format(self.channel, message))

	def process(self, message):
		if '!help' in message:
			self.send("Hi! I'm a Twitch Bot")