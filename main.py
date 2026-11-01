import logging
import os
import asyncio
from threading import Thread
from flask import Flask
import sqlite3
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes
)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("bot_users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        full_name TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_user(user_id, full_name):
    conn = sqlite3.connect("bot_users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR IGNORE INTO users (user_id, full_name) VALUES (?, ?)", (user_id, full_name))
        conn.commit()
    except Exception as e:
        logging.error(f"DB Error: {e}")
    finally:
        conn.close()

def get_all_users():
    conn = sqlite3.connect("bot_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]

app = Flask('')

@app.route('/')
def home():
    return "Jetqueen Bot is Alive and Running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

TOKEN = "9287218663:AAEq5ggjRCD8lP0NwVAYYiKcs3Bh2nIjdAo"

async def send_welcome_sequence(bot, user_id, full_name):
    try:
        # 1. Welcome Message 1
        welcome_text_1 = (
            "🤍 **Hey JetQueen Community** ❤️‍🔥\n\n"
            "🙂 Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! 💰\n\n"
            "Start today with just 2000 minimum deposit\n"
            "use Promo Code: DS745 and unlock your full earning potential\n"
            "🚀\n\n"
            "👉 Create your account now:\n"
            "🌐 https://lkhe.cc/3e6ff0\n"
            "🌐 https://lkhe.cc/3e6ff0\n\n"
            "🎁 Promo code:- DS745 ✔️\n\n"
            "Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke 💖\n\n"
            "Join us and fly high with Aviator\n"
            "🚀\n"
            "Let’s make your next game your biggest win!... ❤️‍🔥"
        )
        IMAGE_1_URL = "https://i.postimg.cc/mk2bFfwN/IMG-3600.jpg"
        
        await bot.send_photo(chat_id=user_id, photo=IMAGE_1_URL, caption=welcome_text_1, parse_mode="Markdown")
        await asyncio.sleep(1)

        # 2. Welcome Message 2
        welcome_text_2 = (
            "🚨 Want to join PRIME Channel for FREE? Here's how: 📌\n\n"
            "1️⃣ Create a fresh new account on 1win\n"
            "INDIA 🇮🇳 & GLOBAL LINK 🔗\n\n"
            "https://lkhe.cc/3e6ff0\n"
            "https://lkhe.cc/3e6ff0\n\n"
            "📌 Use promo code : DS745 💯‼️\n\n"
            "2️⃣ Deposit 2000 capital 💰\n\n"
            "3️⃣ Send me the ID - @JetQueen_Silpa\n"
            "Vip channel FREE of cost.... 🚀\n\n"
            "🚨Only for serious players who want next-level signals! 💯🚀"
        )
        await bot.send_photo(chat_id=user_id, photo=IMAGE_1_URL, caption=welcome_text_2, parse_mode="Markdown")
        
        logging.info(f"Successfully sent welcome sequence (without voice) to {full_name}")

    except Exception as e:
        logging.error(f"Error in welcome sequence for {user_id}: {e}")

async def accept_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_join_request = update.chat_join_request
    if not chat_join_request:
        return

    try:
        chat = chat_join_request.chat
        user = chat_join_request.from_user

        add_user(user.id, user.full_name)
        await chat_join_request.approve()
        logging.info(f"Approved join request for {user.full_name}")

        asyncio.create_task(send_welcome_sequence(context.bot, user.id, user.full_name))

    except Exception as e:
        logging.error(f"Failed to process join request for user: {e}")

async def welcome_on_join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = update.chat_member
    if not result:
        return

    user = result.new_chat_member.user
    if user.is_bot:
        return

    if result.new_chat_member.status == "member":
        add_user(user.id, user.full_name)
        asyncio.create_task(send_welcome_sequence(context.bot, user.id, user.full_name))

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("⚠️ Message likhna bhul gaye! Use: /broadcast Aapka message yahan")
        return

    message_text = " ".join(context.args)
    users = get_all_users()

    success = 0
    failed = 0

    status_msg = await update.message.reply_text(f"🚀 Broadcasting to {len(users)} users...")

    for user_id in users:
        try:
            await context.bot.send_message(chat_id=user_id, text=message_text, parse_mode="Markdown")
            success += 1
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1

    await status_msg.edit_text(f"✅ Broadcast Done!\n\nSuccess: {success}\nFailed: {failed}")

def main() -> None:
    init_db()
    keep_alive()
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(90)
        .read_timeout(90)
        .write_timeout(90)
        .pool_timeout(90)
        .build()
    )

    application.add_handler(ChatJoinRequestHandler(accept_and_welcome))
    application.add_handler(ChatMemberHandler(welcome_on_join, ChatMemberHandler.CHAT_MEMBER))
    application.add_handler(CommandHandler("broadcast", broadcast))

    print("Bot and web server are running...")
    application.run_polling()

if __name__ == "__main__":
    main()
