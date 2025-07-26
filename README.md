# Motivatsion Xabarlar Boti (Motivational Quotes Bot)

Bu Telegram bot foydalanuvchilarga tasodifiy motivatsion xabarlarni yuborish uchun yaratilgan.

---

This is a simple Telegram bot that sends random motivational quotes to users.

## O'rnatish va Ishga Tushirish (Installation and Usage)

1.  **Loyiha nusxasini oling (Clone the repository):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Virtual muhit yarating va faollashtiring (Create and activate a virtual environment):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Kerakli kutubxonalarni o'rnating (Install dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **`.env` faylini sozlang (Configure the `.env` file):**
    `.env.example` faylidan nusxa olib, `.env` nomli yangi fayl yarating. So'ngra o'zingizning Telegram Bot Tokeningizni kiriting.
    
    Create a new file named `.env` by copying `.env.example` and add your Telegram Bot Token.
    ```
    BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN_HERE"
    ```

5.  **Botni ishga tushiring (Run the bot):**
    ```bash
    python main.py
    ```

## Buyruqlar (Commands)

-   `/start` - Bot bilan salomlashish (Say hello to the bot).
-   `/quote` - Tasodifiy motivatsion xabar olish (Get a random motivational quote).
