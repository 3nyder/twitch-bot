from time import sleep

class Bot:
	#Future bot configs to import???
	def __init__(self, chat, channel, rate):
		"""
	    Start a Bot.
	    Keyword arguments:
	    chat     -- the socket where the chat has been established
	    channel  -- the channel for the Bot to work in
	    rate     -- rate of messages being send
	    """
		self.chat = chat
		self.channel = channel
		self.rate = rate

	def pong(self):
		"""
		For telling the server the bot it's alive.
		"""
		print "PONG"
		self.chat.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
		sleep(1.0 / self.rate)

	def send(self,message):
		"""
	    Send a chat message to the server.
	    Keyword arguments:
	    message  -- the message to be sent
	    """
		self.chat.send("PRIVMSG {} :{}\r\n".format(self.channel, message))
		sleep(1.0 / self.rate)


	def ban(self, user):
		"""
	    Ban a user from the channel
	    Keyword arguments:
	    user -- the user to be sent to timeout
	    """
		self.send(".ban {}".format(user))

	def timeout(self, user, secs=60):
		"""
	    Give a timeout to a user
	    Keyword arguments:
	    user -- the user to be sent to timeout
	    secs -- the seconds of the timeout (default 60)
	    """
		self.send(".timeout {} {}".format(user, secs))

	def process(self, message):
		"""
	    Process a message, kinda main function
	    Keyword arguments:
	    message -- message to be processed
	    """
		if '!help' in message:
			self.send("Hi! I'm a Twitch Bot")