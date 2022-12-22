from telegram.ext import *

import time


API_KEY = "5865465649:AAHwD5JT6Kkj8hyIe_kuQCCCCEZCKDcmn2c"


def start(update, context):
    user_id = str(update.message.from_user.id)

    with open("text.txt") as file:
        lines = [line.rstrip() for line in file]  

    for text in lines:
        context.bot.send_message(text=text, chat_id=user_id)
        time.sleep(1)


def error(update, context):
    print(f"Update {update} caused error.\n {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("Bot started...")

    main()