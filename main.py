import logging
import random
import os
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

# Define a command handler. 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Salom {user.mention_html()}! Men sizga motivatsiya berish uchun yaratilgan botman. /quote buyrug'ini yuboring.",
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random quote."""
    random_quote = random.choice(quotes)
    await update.message.reply_text(random_quote)

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
