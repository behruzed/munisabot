from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7445114497:AAF_wsz3YizU3muzNh3tRe1GomphO1hdhOk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
channel_id = '-1002026177105'

# Inline keyboard for channel subscription
def inline_buttons():
    channel_url = InlineKeyboardButton("Kanalga o'tish", url='https://t.me/egameuz')
    markup = InlineKeyboardMarkup(row_width=1).add(channel_url)
    return markup

# Reply keyboard for subscribed users
buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍"),
    KeyboardButton("Kurs haqida ma'lumot💠"),
    KeyboardButton("Kanalimiz⚡️")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)

    if check_sub_channel['status'] != 'left':
        await message.answer("Siz kanalga a'zo bo`ldingiz☺️", reply_markup=buttons)
    else:
        await message.answer("Assalomu alaykum! Botdan foydalanish uchun iltimos kanalga a'zo bo'ling va /start'ni bosing🙃",
                             reply_markup=inline_buttons())

@dp.callback_query_handler()
async def check_sub(callback: types.CallbackQuery):
    if callback.data == "subdone":
        check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=callback.from_user.id)

        if check_sub_channel['status'] != 'left':
            await callback.message.answer("Siz kanalga a'zo bo`ldingiz☺️", reply_markup=buttons)
        else:
            await callback.message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                                          reply_markup=inline_buttons())

if __name__ == '__main__':
    executor.start_polling(dp)
