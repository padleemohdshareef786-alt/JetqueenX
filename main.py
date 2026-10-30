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

TOKEN = "9287218663:AAHNlXmq3UPTQ5r2rW7PunRrFNO3OXB5FP8"

async def accept_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_join_request = update.chat_join_request
    if not chat_join_request:
        return

    try:
        chat = chat_join_request.chat
        user = chat_join_request.from_user

        await chat_join_request.approve()
        logging.info(f"Approved join request for {user.full_name}")

        welcome_text_1 = (
            f"❤️ Hey {user.first_name} ❤️‍🔥\n\n"
            "🍸 Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! 💰\n\n"
            "Start today with just 2000 minimum deposit\n"
            "use Promo Code: DS745 and unlock your full earning potential 🚀\n\n"
            "👉 Create your account now:\n"
            "🌐 https://lkhe.cc/3e6ff0\n"
            "🌐 https://lkhe.cc/3e6ff0\n\n"
            "🎁 Promo code:- DS745 ✔️\n\n"
            "Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke ❤️\n\n"
            "Join us and fly high with Aviator 🚀\n"
            "Let’s make your next game your biggest win!... ❤️‍🔥"
        )

        IMAGE_1_URL = "https://i.postimg.cc/FzZ11GVQ/IMG-3564.png"
        await context.bot.send_photo(
            chat_id=user.id,
            photo=IMAGE_1_URL,
            caption=welcome_text_1
        )

        welcome_text_2 = (
            "⚠️ Want to join PRIME Channel for FREE? Here's how: 📌\n\n"
            "1️⃣ Create a fresh new account on 1win\n"
            "INDIA😀 & GLOBAL LINK 🔗\n\n"
            "https://lkhe.cc/3e6ff0\n"
            "https://lkhe.cc/3e6ff0\n\n"
            "📌 Use promo code : DS745 💯‼️\n\n"
            "2️⃣ Deposit 2000 capital 💰\n\n"
            "3️⃣ Send me the ID - @JetQueen_Silpa\n"
            "Vip channel FREE of cost.... 🚀\n\n"
            "🚨Only for serious players who want next-level signals! 💯🚀"
        )

        IMAGE_2_URL = "https://i.postimg.cc/85Zq56rQ/IMG-3565.png"
        await context.bot.send_photo(
            chat_id=user.id,
            photo=IMAGE_2_URL,
            caption=welcome_text_2
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
                f"❤️ Hey {user.first_name} ❤️‍🔥\n\n"
                "🍸 Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! 💰\n\n"
                "Start today with just 2000 minimum deposit\n"
                "use Promo Code: DS745 and unlock your full earning potential 🚀\n\n"
                "👉 Create your account now:\n"
                "🌐 https://lkhe.cc/3e6ff0\n"
                "🌐 https://lkhe.cc/3e6ff0\n\n"
                "🎁 Promo code:- DS745 ✔️\n\n"
                "Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke ❤️\n\n"
                "Join us and fly high with Aviator 🚀\n"
                "Let’s make your next game your biggest win!... ❤️‍🔥"
            )

            IMAGE_1_URL = "https://i.postimg.cc/FzZ11GVQ/IMG-356i.png"
            await context.bot.send_photo(
                chat_id=user.id,
                photo=IMAGE_1_URL,
                caption=welcome_text_1
            )

            welcome_text_2 = (
                "⚠️ Want to join PRIME Channel for FREE? Here's how: 📌\n\n"
                "1️⃣ Create a fresh new account on 1win\n"
                "INDIA😀 & GLOBAL LINK 🔗\n\n"
                "https://lkhe.cc/3e6ff0\n"
                "https://lkhe.cc/3e6ff0\n\n"
                "📌 Use promo code : DS745 💯‼️\n\n"
                "2️⃣ Deposit 2000 capital 💰\n\n"
                "3️⃣ Send me the ID - @JetQueen_Silpa\n"
                "Vip channel FREE of cost.... 🚀\n\n"
                "🚨Only for serious players who want next-level signals! 💯🚀"
            )

            IMAGE_2_URL = "https://i.postimg.cc/85Zq56rQ/IMG-3565.png"
            await context.bot.send_photo(
                chat_id=user.id,
                photo=IMAGE_2_URL,
                caption=welcome_text_2
            )

            logging.info(f"Sent manual welcome images to {user.full_name}")
        except Exception as e:
            logging.error(f"Failed to send manual welcome message: {e}")

def main() -> None:
    keep_alive()
    application = ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).write_timeout(30).build()

    application.add_handler(ChatJoinRequestHandler(accept_and_welcome))
    application.add_handler(ChatMemberHandler(welcome_on_join, ChatMemberHandler.CHAT_MEMBER))

    print("Bot and web server are running...")
    application.run_polling()

if __name__ == "__main__":
    main()
