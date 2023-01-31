import logging
import os

import telegram
from telegram import InputFile
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def create_sticker(update, context):
    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    new_file = context.bot.get_file(file_id)
    new_file.download('sticker.png')
    context.bot.create_new_sticker_set(
        user_id=chat_id,
        name='sticker_set_name',
        title='Sticker Set Title',
        png_sticker=open('sticker.png', 'rb'),
        emojis='😀'
    )
    os.remove('sticker.png')
    update.message.reply_text("Sticker created successfully!")

def main():
    updater = Updater("BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("create_sticker", create_sticker))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
