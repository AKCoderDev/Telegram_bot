from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext)-> None:
    user = update.effective_user
    user_info = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "language_code": user.language_code,
    }

    logging.info(f"User info:{user_info}")

    update.message.reply_text(f"
                              Привет,{user.first_name}! Спасибо, что воспользовались ботом!"
                              )


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

update.message.reply_text(f"Вы сказали: {update.message.text}")

def main():
    
    updater = Updater("YOUR_TOKEN")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()