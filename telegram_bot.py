from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import string

TELEGRAM_BOT_TOKEN = '7431080630:AAF2hwY4kHx5vM2CICErQ0cdJe_Aaq8cmtg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Вітаю! Введіть команду /get_password для отримання паролю.')

async def get_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    await update.message.reply_text(f'Ваш пароль: {password}')

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_password", get_password))

    application.run_polling()

if __name__ == '__main__':
    main()
