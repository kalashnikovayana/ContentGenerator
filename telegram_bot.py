from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import string

TELEGRAM_BOT_TOKEN = '7431080630:AAF2hwY4kHx5vM2CICErQ0cdJe_Aaq8cmtg'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Вітаю! Введіть команду /get_password для отримання паролю.')

def get_password(update: Update, context: CallbackContext) -> None:
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    update.message.reply_text(f'Ваш пароль: {password}')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_password", get_password))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
