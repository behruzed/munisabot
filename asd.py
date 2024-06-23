from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

buttons = ReplyKeyboardMarkup([["Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍"], ["Kurs haqida ma'lumot💠"]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Salom, {update.effective_user.first_name} botga xush kelibsiz', reply_markup=buttons)


app = ApplicationBuilder().token("  ").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()