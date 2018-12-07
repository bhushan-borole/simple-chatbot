from chatterbot import ChatBot
bot = ChatBot('My_Bot')


def main():
	while True:
		msg = input('You: ')
		if msg == 'Bye' or msg == 'exit':
			break
		reply = bot.get_response(msg)
		print(str(bot.name) + ':' + str(reply))

if __name__ == '__main__':
	main()