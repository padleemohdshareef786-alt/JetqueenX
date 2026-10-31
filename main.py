import logging
import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ChatMemberHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

app = Flask('')

@app.route('/')
def home():
    return "Jetqueen Bot is Alive and Running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

TOKEN = "9287218663:AAFmqT7jO4jfYbEJ68rr66J76A0KttEBVjQ"

async def accept_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_join_request = update.chat_join_request
    if not chat_join_request:
        return

    try:
        chat = chat_join_request.chat
        user = chat_join_request.from_user

        await chat_join_request.approve()
        logging.info(f"Approved join request for {user.full_name}")

        # Pehla Welcome Message (Screenshot 6 ke exact text aur animated emojis ke sath)[span_2](start_span)[span_2](end_span)
        welcome_text_1 = (
            f"<tg-emoji emoji-id=\"6334860759104755103\">🤍</tg-emoji> **Hey JetQueen Community** <tg-emoji emoji-id=\"6334860759104755103\">❤️‍🔥</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🤨</tg-emoji> Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! <tg-emoji emoji-id=\"6334860759104755103\">💰</tg-emoji>\n\n"
            "Start today with just 2000 minimum deposit\n"
            "use Promo Code: DS745 and unlock your full earning potential\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">👉</tg-emoji> Create your account now:\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🌐</tg-emoji> https://lkhe.cc/3e6ff0\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🌐</tg-emoji> https://lkhe.cc/3e6ff0\n\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🎁</tg-emoji> Promo code:- DS745 <tg-emoji emoji-id=\"6334860759104755103\">✔️</tg-emoji>\n\n"
            "Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke <tg-emoji emoji-id=\"6334860759104755103\">💖</tg-emoji>\n\n"
            "Join us and fly high with Aviator\n"
            "<tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n"
            "Let’s make your next game your biggest win!... <tg-emoji emoji-id=\"6334860759104755103\">❤️‍🔥</tg-emoji>"
        )

        IMAGE_1_URL = "https://chatgpt.com/s/m_6ae4e862ecb08191ba6b6a83c0723ed6"
        await context.bot.send_photo(
            chat_id=user.id,
            photo=IMAGE_1_URL,
            caption=welcome_text_1,
            parse_mode="HTML"
        )

        # Doosra Welcome Message (Screenshot 4 ke exact text aur animated emojis ke sath)[span_3](start_span)[span_3](end_span)
        welcome_text_2 = (
            "<tg-emoji emoji-id=\"6334870895227573067\">🚨</tg-emoji> Want to join PRIME Channel for FREE? Here's how: <tg-emoji emoji-id=\"6332267526570906235\">📌</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"5305763715692377402\">1️⃣</tg-emoji> Create a fresh new account on 1win\n"
            "INDIA <tg-emoji emoji-id=\"6136551252781172945\">🇮🇳</tg-emoji> & GLOBAL LINK <tg-emoji emoji-id=\"5271604874419647061\">🔗</tg-emoji>\n\n"
            "https://lkhe.cc/3e6ff0\n"
            "https://lkhe.cc/3e6ff0\n\n"
            "<tg-emoji emoji-id=\"5397782960512444700\">📌</tg-emoji> Use promo code : DS745 <tg-emoji emoji-id=\"5341498088408234504\">💯</tg-emoji><tg-emoji emoji-id=\"6332595047891997036\">‼️</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"5307907239380528763\">2️⃣</tg-emoji> Deposit 2000 capital <tg-emoji emoji-id=\"6332375519228597344\">💰</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"5305783000095537258\">3️⃣</tg-emoji> Send me the ID - @JetQueen_Silpa\n"
            "Vip channel FREE of cost.... <tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n\n"
            "<tg-emoji emoji-id=\"5395695537687123235\">🚨</tg-emoji>Only for serious players who want next-level signals! <tg-emoji emoji-id=\"5341498088408234504\">💯</tg-emoji><tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>"
        )

        IMAGE_2_URL = "https://chatgpt.com/s/m_6ae4e85828808191891657bbc3bdcbff"
        await context.bot.send_photo(
            chat_id=user.id,
            photo=IMAGE_2_URL,
            caption=welcome_text_2,
            parse_mode="HTML"
        )

        logging.info(f"Sent welcome images and messages to {user.full_name}")

    except Exception as e:
        logging.error(f"Failed to process join request for {user.id}: {e}")

async def welcome_on_join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = update.chat_member
    if not result:
        return

    user = result.new_chat_member.user
    if user.is_bot:
        return

    if result.new_chat_member.status == "member":
        try:
            welcome_text_1 = (
                f"<tg-emoji emoji-id=\"6334860759104755103\">🤍</tg-emoji> **Hey JetQueen Community** <tg-emoji emoji-id=\"6334860759104755103\">❤️‍🔥</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🤨</tg-emoji> Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! <tg-emoji emoji-id=\"6334860759104755103\">💰</tg-emoji>\n\n"
                "Start today with just 2000 minimum deposit\n"
                "use Promo Code: DS745 and unlock your full earning potential\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">👉</tg-emoji> Create your account now:\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🌐</tg-emoji> https://lkhe.cc/3e6ff0\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🌐</tg-emoji> https://lkhe.cc/3e6ff0\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🎁</tg-emoji> Promo code:- DS745 <tg-emoji emoji-id=\"6334860759104755103\">✔️</tg-emoji>\n\n"
                "Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke <tg-emoji emoji-id=\"6334860759104755103\">💖</tg-emoji>\n\n"
                "Join us and fly high with Aviator\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n"
                "Let’s make your next game your biggest win!... <tg-emoji emoji-id=\"6334860759104755103\">❤️‍🔥</tg-emoji>"
            )

            IMAGE_1_URL = "https://chatgpt.com/s/m_6ae4e862ecb08191ba6b6a83c0723ed6"
            await context.bot.send_photo(
                chat_id=user.id,
                photo=IMAGE_1_URL,
                caption=welcome_text_1,
                parse_mode="HTML"
            )

            welcome_text_2 = (
                "<tg-emoji emoji-id=\"6334860759104755103\">🚨</tg-emoji> Want to join PRIME Channel for FREE? Here's how: <tg-emoji emoji-id=\"6334860759104755103\">📌</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">1️⃣</tg-emoji> Create a fresh new account on 1win\n"
                "INDIA <tg-emoji emoji-id=\"6334860759104755103\">🇮🇳</tg-emoji> & GLOBAL LINK <tg-emoji emoji-id=\"6334860759104755103\">🔗</tg-emoji>\n\n"
                "https://lkhe.cc/3e6ff0\n"
                "https://lkhe.cc/3e6ff0\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">📌</tg-emoji> Use promo code : DS745 <tg-emoji emoji-id=\"6334860759104755103\">💯</tg-emoji><tg-emoji emoji-id=\"6334860759104755103\">‼️</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">2️⃣</tg-emoji> Deposit 2000 capital <tg-emoji emoji-id=\"6334860759104755103\">💰</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">3️⃣</tg-emoji> Send me the ID - @JetQueen_Silpa\n"
                "Vip channel FREE of cost.... <tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>\n\n"
                "<tg-emoji emoji-id=\"6334860759104755103\">🚨</tg-emoji>Only for serious players who want next-level signals! <tg-emoji emoji-id=\"6334860759104755103\">💯</tg-emoji><tg-emoji emoji-id=\"6334860759104755103\">🚀</tg-emoji>"
            )

            IMAGE_2_URL = "https://chatgpt.com/s/m_6ae4e85828808191891657bbc3bdcbff"
            await context.bot.send_photo(
                chat_id=user.id,
                photo=IMAGE_2_URL,
                caption=welcome_text_2,
                parse_mode="HTML"
            )

            logging.info(f"Sent manual welcome images to {user.full_name}")
        except Exception as e:
            logging.error(f"Failed to send manual welcome message: {e}")

def main() -> None:
    keep_alive()
    application =ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).write_timeout(30).build()

    application.add_handler(ChatJoinRequestHandler(accept_and_welcome))
    application.add_handler(ChatMemberHandler(welcome_on_join, ChatMemberHandler.CHAT_MEMBER))

    print("Bot and web server are running...")
    application.run_polling()

if __name__ == "__main__":
    main()


