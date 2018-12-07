from chatterbot import ChatBot
bot = ChatBot('My_Bot')


def main():
	while True:
		msg = input('You: ')
		if msg.strip() != 'Bye':
			result = bot.get_response(msg)                        
			reply = str(result)
			print(reply)
		if msg.strip() == 'Bye':
			print('Bye')
			break

if __name__ == '__main__':
	main()