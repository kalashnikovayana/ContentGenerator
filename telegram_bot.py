from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Встановлюємо ваш Telegram Bot Token
TELEGRAM_BOT_TOKEN = '7431080630:AAEEH75kxiSGxTz9HAQ3xzc4hnSIRXvYOq8'

# Встановлюємо логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Визначаємо команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Введіть команду /get_password для отримання паролю.')

def main() -> None:
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # Додаємо обробник для команди /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаємо бота
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()




