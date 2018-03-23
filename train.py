from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatterbot = ChatBot("Iniya")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("chatterbot.corpus.english")
