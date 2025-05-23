# Easy Telegram Bot

This project is a simple Telegram bot built using the [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html) library. The bot can greet users and echo back any message it receives.

## Features

- Responds to `/start` and `/hello` commands with a welcome message.
- Echoes any text message sent by the user.

## Getting Started

### Prerequisites

- Python 3.13
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

### Installation

1. Install the required library:
    ```
    uv add pyTelegramBotAPI
    ```

2. Obtain a Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather).

### Usage

1. Replace `"your_token_here"` in the code with your actual bot token.
2. Run the script:
    ```
    python your_script.py
    ```

### Example Code

```python
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
```

