from handlers.index import index
from telegram.ext import Updater, CommandHandler
from configuration import Config

config = Config('configuration.yaml')
config.show_label()

def main():
    
    updater = Updater(config.token)
    dp = updater.dispatcher
    for k,v in index().items():
        dp.add_handler(CommandHandler(k, v))
    updater.start_polling()
    updater.idle()

main()