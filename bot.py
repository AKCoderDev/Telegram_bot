from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import logging

#logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#function for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
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

    await update.message.reply_text(
        f"Hello,{user.first_name}! How are you {user.first_name}?"
        )

#function for processing any words
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
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
    await update.message.reply_text(f"You say: {update.message.text}")

#main function
def main():
    #your token
    TOKEN = ("your token")
     # Create the Application
    app = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    app.run_polling()

if __name__== '__main__':
    main()
