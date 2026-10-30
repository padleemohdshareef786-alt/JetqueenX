import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# Enable logging
logging.basicConfig(
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
level=logging.INFO
)

TOKEN = "9287218663:AAGNm93OSewMkxOHgnKDnX7TKJY1jIO-Xmc" # Yahan apna token paste karna (quotes ke andar hi rehne dena)

async def accept_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
chat_join_request = update.chat_join_request
if not chat_join_request:
return

chat = chat_join_request.chat
user = chat_join_request.from_user

try:
# 1. Automatically approve the join request
await chat.approve_chat_join_request(user.id)
logging.info(f"Approved join request for {user.full_name}")

# 2. Your custom welcome message
welcome_text = (
f"❤️ Hey {user.first_name} ❤️‍🔥\n\n"
"🍸 Say goodbye to random guesses — JetQueen's proven strategies and smart analysis will help you grow your balance like never before! 💰\n\n"
"Start today with just 2000 minimum deposit \n"
"use Promo Code: **DS745** and unlock your full earning potential 🚀\n\n"
"👉 Create your account now:\n"
"🌐 https://lkhe.cc/3e6ff0\n\n"
"🎁 Promo code:- `DS745` ✔️\n\n"
"Message me ID number......me guide karungi apko ki kese earn karna hai bina loss or sahi money management karke ❤️\n\n"
"Join us and fly high with Aviator 🚀\n"
"Let’s make your next game your biggest win!... ❤️‍🔥\n\n\n"
"⚠️ Want to join PRIME Channel for FREE? Here's how: 📌\n\n"
"1️⃣ Create a fresh new account on 1win\n"
"INDIA😀 & GLOBAL LINK 🔗\n"
"https://lkhe.cc/3e6ff0\n\n"
"📌 Use promo code : `DS745` 💯‼️\n\n"
"2️⃣ Deposit 2000 capital 💰\n\n"
"3️⃣ Send me the ID - @JetQueen_Silpa\n"
"Vip channel FREE of cost.... 🚀\n\n"
"🚨Only for serious players who want next-level signals! 💯🚀"
)

# Send it directly to the user's private messages
await context.bot.send_message(
chat_id=user.id,
text=welcome_text,
parse_mode="Markdown"
)
logging.info(f"Sent welcome message to {user.full_name}")

except Exception as e:
logging.error(f"Failed to process join request for {user.id}: {e}")

def main() -> None:
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(ChatJoinRequestHandler(accept_and_welcome))
print("Bot is running...")
application.run_polling()

if __name__ == "__main__":
main()


