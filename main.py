from config import *
from bot import *
import socket
import time

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

#Initialize the bot
bot = Bot(s, CHAN, RATE)

while True:
	#example line from recv
    #:3nyder_bot!3nyder_bot@3nyder_bot.tmi.twitch.tv PRIVMSG #3nyder :bot to app
    response = s.recv(1024).decode("utf-8")

    print(response)

    lines = response.split('\r\n')
    for line in lines:
    	line_arr = line.split(':')
    	if len(line_arr) > 1:
	    	message = line_arr[-1]
	    	user_info = line_arr[1]
	    	user_info = user_info.split('!')
	    	if len(user_info) > 1:
	    		user = user_info[0]
	    		bot.process(message)

    time.sleep(0.1)