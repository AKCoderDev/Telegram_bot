from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

#logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#function for /start
def start(update: Update, context: CallbackContext)-> None:
    user = update.effective_user
    user_info = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "language_code": user.language_code,
    }
#logging information about user
    logging.info(f"User info:{user_info}")

    update.message.reply_text(f"
                              Привет,{user.first_name}! Спасибо, что воспользовались ботом!"
                              )

#function for processing any words
def echo(update: Update, context: CallbackContext)-> None:
    user = update.effective_user
    user_info = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "language_code": user.language_code,
    }

logging.info(f"User message info: {user_info}")

#answer message
update.message.reply_text(f"Вы сказали: {update.message.text}")

#main function
def main():
    #your token
    updater = Updater("YOUR_TOKEN")
    #registration  processing
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()