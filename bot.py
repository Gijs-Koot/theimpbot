from telegram.ext import Updater, CommandHandler
import json
import random
import code

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')

def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.first_name))

def quote(bot, update):
    bot.sendMessage(update.message.chat_id, text=random.choice(quotes))

with open('./quotes.txt') as f: quotes = json.load(f)

updater = Updater(code.api_code)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('q', quote))

updater.start_polling()
updater.idle()
