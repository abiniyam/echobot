from telegram.ext import Updater, CommandHandler

token = "306226834:AAG23HIKPbvhSKsFpMyIREdfUOnArEDUwRs"
URL = "https://api.telegram.org/bot{}/".format(token)

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
