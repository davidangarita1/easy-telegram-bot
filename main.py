import telebot

BOT_TOKEN = "your_token_here"  # Replace with your actual bot token

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
