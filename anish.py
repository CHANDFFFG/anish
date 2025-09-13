from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import re

# Replace this with your actual bot token
BOT_TOKEN = '7508809039:AAG2MaWkfdaJipxSBZ1HDI5DkL7Zl-CDOpk'

# Keywords to detect
KEYWORDS = ['dm karo', 'DM me aao', 'message karo', 'inbox aao']

# Function to handle messages
async def delete_keyword_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()

    # Check for keywords
    if any(keyword in message_text for keyword in KEYWORDS):
        await update.message.delete()
        return

    # Check for usernames (like @username)
    if re.search(r'@\w+', update.message.text):
        await update.message.delete()

# Main setup
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), delete_keyword_messages)
    app.add_handler(handler)
    app.run_polling()