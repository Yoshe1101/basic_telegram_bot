import json
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
#reading the credentials from secure plase
f = open('/home/joseba/credentials/keys.json',)
data = json.load(f)
token = data["keys"]["telegram_key"]


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

# def foto(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     send_foto(update.message.chat_id,'https://i1.wp.com/www.sopitas.com/wp-content/uploads/2012/06/chuck_norris__-e1469703347157.jpg)

def mensajes(update: Update, context: CallbackContext) -> None:
    random_number = random.randint(0,9)
    print(random_number)
    if random_number == 2:
        update.message.reply_text("TE REVIENTO!!!")
        #telegram.InputMediaDocument('images/chuck_norris__-e1469703347157.jpg')
    else:
        frases = ["Pues ok","muy bien","ahora no tengo tiempo","mañana lo miramos"]
        update.message.reply_text(random.choice(frases))
    

# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("foto", foto))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, mensajes))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()