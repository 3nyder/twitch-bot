from time import sleep

class Bot:
	#Future bot configs to import???

	active_polls = {}

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

	def start_poll(self, user, poll_options):
		"""
		Start a poll with options
	    Keyword arguments:
	    user 		 -- the user that started the poll
	    poll_options -- command and options to use in the poll (example "!poll opt1 opt2 ... optn")
	    """
		poll_options_arr = poll_options.split(" ")
		if len(poll_options_arr) <= 1 or poll_options_arr[0] != "!poll":
			self.send(user + ' polls can be started with "!poll opt1 opt2 ... optn"')
			return

		if user in self.active_polls.keys():
			self.send(user + " you have an active poll, finish it with !endpoll")
			return
		
		self.active_polls[user] = {}

		for option in poll_options_arr[1:]:
			self.active_polls[user][option] = 0	

		self.send(user + " started a poll")

	#TODO: check what users already voted
	def vote_poll(self, user, vote):
		"""
		Start a poll with options
		Keyword arguments:
		user -- the user that voted
		vote -- command, user and vote (example "!vote usr option")
		"""
		vote_arr = vote.split(" ")
		if len(vote_arr) <= 1 or vote_arr[0] != "!vote":
			self.send(user + ' you can vote with "!vote usr option"')
			return

		if vote_arr[1] not in self.active_polls.keys():
			self.send(user + ", " + vote_arr[1] + " doesn't have an active poll")
			return

		if vote_arr[2] not in self.active_polls[vote_arr[1]].keys():
			self.send(user + ", " + vote_arr[2] + " that's not an option")
			return

		self.active_polls[vote_arr[1]][vote_arr[2]] += 1

	def end_poll(self,user):
		"""
		Start a poll with options
		Keyword arguments:
		user 		 -- the user that started the poll
		"""
		if user not in self.active_polls.keys():
			self.send(user + ' you don\'t have any poll, they can be started with "!poll opt1 opt2 ... optn"')
			return

		poll_sum = 0
		for option in self.active_polls[user]:
			poll_sum += self.active_polls[user][option]

		self.send(user + ' poll got ' + str(poll_sum) + " votes and the results are")
		results_arr = []
		for option in self.active_polls[user]:
			votes = self.active_polls[user][option] + 0.0
			percent = "%.2f" % ((votes/poll_sum)*100)
			results_arr.append(option + ": " + percent + "%")

		results = " | ".join(results_arr)
		self.send(results)

	def process(self, user, message):
		"""
	    Process a message, kinda main function
	    Keyword arguments:
	    message -- message to be processed
	    """
		if '!help' in message:
			self.send("Hi! I'm a Twitch Bot")

		if '!poll' in message:
			self.start_poll(user, message)

		if '!endpoll' in message:
			self.end_poll(user)

		if '!vote' in message:
			self.vote_poll(user,  message)