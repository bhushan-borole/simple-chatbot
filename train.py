from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def train(bot):
	path = 'data\\english\\'
	for file in os.listdir(path):
		data = open(path + file, 'r').readlines()
		bot.train(data)

def main():
	bot = ChatBot('My_Bot')
	bot.set_trainer(ListTrainer)
	train(bot)


if __name__ == '__main__':
	main()

