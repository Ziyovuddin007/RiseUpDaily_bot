import logging
import random
import os
import json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

STATE_FILE = "bot_state.json"

# Load quotes from a file
try:
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        quotes = [line.strip() for line in f.readlines() if line.strip()]
    if not quotes:
        logger.error("'quotes.txt' file is empty.")
        quotes = ["Ma'lumotlar bazasi bo'sh. Iltimos, administrator bilan bog'laning."]
except FileNotFoundError:
    logger.error("'quotes.txt' not found.")
    quotes = ["Xatolik: Motivatsion xabarlar fayli topilmadi."]


def load_state():
    """Loads the bot state from a JSON file."""
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"last_quote_index": 0}


def save_state(state):
    """Saves the bot state to a JSON file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

# Define a command handler. 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Salom {user.mention_html()}! Men sizga motivatsiya berish uchun yaratilgan botman. /quote buyrug'ini yuboring.",
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the next quote in sequence."""
    state = load_state()
    current_index = state.get("last_quote_index", 0)

    # Ensure index is within bounds
    if current_index >= len(quotes):
        current_index = 0

    quote_to_send = quotes[current_index]
    await update.message.reply_text(quote_to_send)

    # Update the state for the next quote
    next_index = (current_index + 1) % len(quotes)
    save_state({"last_quote_index": next_index})

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text(
        "Salom! Men sizga motivatsiya berish uchun yaratilganman.\n\n" \
        "Mavjud buyruqlar:\n" \
        "/start - Botni ishga tushirish\n" \
        "/quote - Tasodifiy motivatsion xabar olish\n" \
        "/help - Yordam ma'lumotlarini ko'rish"
    )

def main() -> None:
    """Start the bot."""
    # Get the bot token from environment variables
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Bot token not found. Please set the BOT_TOKEN in your .env file.")

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
