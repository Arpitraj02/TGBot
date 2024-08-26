from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace with your actual Telegram Bot token
TELEGRAM_TOKEN = '7526431032:AAFvR0YV-2OtKQN_hzrL5mz8iZNpSu-or7o'

# Predefined YouTube links for coding tutorials
tutorial_links = {
    "Python": [
        ("Python Crash Course for Beginners", "https://www.youtube.com/watch?v=rfscVS0vtbw"),
        ("Python Tutorial - Python for Beginners", "https://www.youtube.com/watch?v=_uQrJ0TkZlc"),
        ("Python Full Course - Learn Python in 12 Hours", "https://www.youtube.com/watch?v=WGJJIrtnfpk"),
        ("Python Programming for Beginners", "https://www.youtube.com/watch?v=8DvywoWv6fI"),
        ("Learn Python - Full Course for Beginners", "https://www.youtube.com/watch?v=rfscVS0vtbw"),
    ],
    "JavaScript": [
        ("JavaScript Crash Course", "https://www.youtube.com/watch?v=PkZNo7MFNFg"),
        ("Learn JavaScript in 1 Hour", "https://www.youtube.com/watch?v=W6NZfCO5SIk"),
        ("JavaScript Tutorial for Beginners", "https://www.youtube.com/watch?v=hdI2bqOjy3c"),
        ("JavaScript Full Course for Beginners", "https://www.youtube.com/watch?v=Qqx_wzMmFeA"),
        ("JavaScript Essentials for Absolute Beginners", "https://www.youtube.com/watch?v=G3e-cpL7ofc"),
    ],
    "Java": [
        ("Java Tutorial for Beginners", "https://www.youtube.com/watch?v=eIrMbAQSU34"),
        ("Learn Java in 14 Minutes", "https://www.youtube.com/watch?v=RRubcjpTkks"),
        ("Java Full Course - Learn Java in 8 Hours", "https://www.youtube.com/watch?v=grEKMHGYyns"),
        ("Java Programming - Full Course", "https://www.youtube.com/watch?v=GoXwIVyNvX0"),
        ("Java for Beginners - A Complete Guide", "https://www.youtube.com/watch?v=8cm1x4bC610"),
    ],
    "C++": [
        ("C++ Tutorial for Beginners", "https://www.youtube.com/watch?v=vLnPwxZdW4Y"),
        ("Learn C++ in One Video", "https://www.youtube.com/watch?v=K4FK6dxQBBk"),
        ("C++ Full Course - Learn C++ in 10 Hours", "https://www.youtube.com/watch?v=mUQZ1qmKlLY"),
        ("C++ Programming in 4 Hours", "https://www.youtube.com/watch?v=ZzaPdXTrSb8"),
        ("C++ Programming Language Tutorial", "https://www.youtube.com/watch?v=Rub-JsjMhWY"),
    ],
    "HTML & CSS": [
        ("HTML Full Course - Build a Website", "https://www.youtube.com/watch?v=pQN-pnXPaVg"),
        ("Learn HTML & CSS - Full Course", "https://www.youtube.com/watch?v=mU6anWqZJcc"),
        ("HTML & CSS Crash Course", "https://www.youtube.com/watch?v=UB1O30fR-EE"),
        ("HTML & CSS for Beginners", "https://www.youtube.com/watch?v=qz0aGYrrlhU"),
        ("Responsive Web Design Tutorial", "https://www.youtube.com/watch?v=srvUrASNj0s"),
    ],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("Python", callback_data='Python')],
        [InlineKeyboardButton("JavaScript", callback_data='JavaScript')],
        [InlineKeyboardButton("Java", callback_data='Java')],
        [InlineKeyboardButton("C++", callback_data='C++')],
        [InlineKeyboardButton("HTML & CSS", callback_data='HTML & CSS')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to the YouTube Search Bot! Choose a topic to see the best coding tutorials:",
        reply_markup=reply_markup
    )

async def show_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with YouTube tutorial links based on the selected topic."""
    query = update.callback_query
    await query.answer()
    
    topic = query.data
    links = tutorial_links.get(topic, [])
    
    if links:
        response = f"Here are some great {topic} tutorials:\n\n"
        for title, url in links:
            response += f"[{title}]({url})\n"
        await query.edit_message_text(text=response, parse_mode='Markdown')
    else:
        await query.edit_message_text(text="Sorry, no tutorials available for this topic.")

def main() -> None:
    """Start the bot."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(show_links))

    # Start polling for updates from Telegram
    app.run_polling()

if __name__ == '__main__':
    main()
