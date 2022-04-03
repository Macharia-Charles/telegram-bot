from . import constants as kt
from . import responses as rs
from telegram.ext import *


print("Starting bot.....")


def start_command(update, context):
    update.message.reply_text("Type something random.")


def help_command(update, context):
    update.message.reply_text("Visit our shop for help")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = rs.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(kt.API_KEY, use_context=True)
    dispatch = updater.dispatcher

    dispatch.add_handler(CommandHandler('Start', start_command))
    dispatch.add_handler(CommandHandler('Help', help_command))

    dispatch.add_handler(MessageHandler(Filters.text, handle_message))

    dispatch.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()