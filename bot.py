class Bot:
	#Future bot configs to import???
	def __init__(self, chat, channel):
		"""
	    Start a Bot.
	    Keyword arguments:
	    chat     -- the socket where the chat has been established
	    channel  -- the channel for the Bot to work in
	    """
		self.chat = chat
		self.channel = channel

	def send(self,message):
		"""
	    Send a chat message to the server.
	    Keyword arguments:
	    message  -- the message to be sent
	    """
		self.chat.send("PRIVMSG {} :{}\r\n".format(self.channel, message))

	def timeout(self, user, secs=60):
		"""
	    Give a timeout to a user
	    Keyword arguments:
	    user -- the user to be sent to timeout
	    secs -- the seconds of the timeout (default 60)
	    """
		slef.send(".timeout {} {}".format(user, secs))

	def process(self, message):
		"""
	    Process a message, kinda main function
	    Keyword arguments:
	    message -- message to be processed
	    """
		if '!help' in message:
			self.send("Hi! I'm a Twitch Bot")
		if '!testban' in message:
			self.ban("3nyder_bot", 30)