from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = "7445114497:AAF_wsz3YizU3muzNh3tRe1GomphO1hdhOk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

channel_id = '-1002071497608'

# Inline keyboard for channel subscription
def inline_buttons():
    channel_url = InlineKeyboardButton("Kanalga o'tish", url='https://t.me/munisa_onlinesavdo_wechat')
    markup = InlineKeyboardMarkup(row_width=1).add(channel_url)
    return markup

# Reply keyboard for subscribed users
buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton("Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍")
).row(
    KeyboardButton("Kurs haqida ma'lumot💠")
).row(
    KeyboardButton("Kanalimiz⚡️")
)

# Back button keyboard
back_button = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton("Orqaga qaytish🔙")
)

async def check_subscription(user_id):
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    return member.status != 'left'

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        await message.answer("Siz kanalga a'zo bo'lgansiz☺️", reply_markup=buttons)
    else:
        await message.answer("Assalomu alaykum! Botdan foydalanish uchun iltimos kanalga a'zo bo'ling va /start'ni bosing🙃",
                             reply_markup=inline_buttons())

@dp.message_handler(lambda message: message.text == "Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍")
async def order_info(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if (is_subscribed):
        await message.answer("Davlatni tanlang:", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).row(
            KeyboardButton("🇨🇳Xitoy davlatidan tovar buyurtma qilishning 5 ta foydali tomoni")
        ).row(
            KeyboardButton("🇹🇷Turkiya davlatidan tovar buyurtma qilishning 3 ta foydali tomoni")
        ).row(
            KeyboardButton("💥iHerb dasturi orqali chegirmalardan foydalanish")
        ).row(
            KeyboardButton("🛂Bojxona haqida")
        ).row(
            KeyboardButton("💠Mustaqil buyurtma berish")
        ).row(
            KeyboardButton("🏘Uyda o`tirgan holda daromad")
        ).row(
            KeyboardButton("Orqaga qaytish🔙")
        ))
    else:
        await message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                             reply_markup=inline_buttons())

async def forward_message(chat_id, message_id, target_chat_id):
    try:
        await bot.forward_message(chat_id=chat_id, from_chat_id=target_chat_id, message_id=message_id)
    except Exception as e:
        print(f"Error: {e}")

@dp.message_handler(lambda message: message.text == "🇨🇳Xitoy davlatidan tovar buyurtma qilishning 5 ta foydali tomoni")
async def china_info(message: types.Message):
    await forward_message(message.chat.id, 112, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "🇹🇷Turkiya davlatidan tovar buyurtma qilishning 3 ta foydali tomoni")
async def turkey_info(message: types.Message):
    await forward_message(message.chat.id, 217, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "💥iHerb dasturi orqali chegirmalardan foydalanish")
async def iherb_info(message: types.Message):
    await forward_message(message.chat.id, 52, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "🛂Bojxona haqida")
async def customs_info(message: types.Message):
    await forward_message(message.chat.id, 279, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "💠Mustaqil buyurtma berish")
async def independent_order_info(message: types.Message):
    await forward_message(message.chat.id, 292, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "🏘Uyda o`tirgan holda daromad")
async def home_income_info(message: types.Message):
    await forward_message(message.chat.id, 314, '@munisa_onlinesavdo_wechat')
    await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@dp.message_handler(lambda message: message.text == "Kurs haqida ma'lumot💠")
async def course_info(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        links = [
            ("behruzqwe", 2),
            ("behruzqwe", 3),
            ("behruzqwe", 4)
        ]
        for chat_id, message_id in links:
            try:
                msg = await bot.forward_message(chat_id=message.chat.id, from_chat_id=f"@{chat_id}", message_id=message_id)
            except Exception as e:
                print(f"Error: {e}")
        await message.answer("Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)
    else:
        await message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                             reply_markup=inline_buttons())

@dp.message_handler(lambda message: message.text == "Kanalimiz⚡️")
async def channel_info(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        await message.answer("Telegram kanal:", reply_markup=inline_buttons())
    else:
        await message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                             reply_markup=inline_buttons())

@dp.message_handler(lambda message: message.text == "Orqaga qaytish🔙")
async def go_back(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        await message.answer("Bosh sahifaga qaytdingiz", reply_markup=buttons)
    else:
        await message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                             reply_markup=inline_buttons())

@dp.message_handler()
async def handle_message(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        # Handle other messages from subscribed users here
        await message.answer("Siz kanalga a'zo bo'lgansiz. Tugmalarni ishlatishingiz mumkin.", reply_markup=buttons)
    else:
        await message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                             reply_markup=inline_buttons())

@dp.callback_query_handler()
async def check_sub(callback: types.CallbackQuery):
    if callback.data == "subdone":
        is_subscribed = await check_subscription(callback.from_user.id)

        if is_subscribed:
            await callback.message.answer("Siz kanalga a'zo bo'lgansiz☺️", reply_markup=buttons)
        else:
            await callback.message.answer("Botdan foydalanish uchun iltimos kanalga a'zo bo'ling",
                                          reply_markup=inline_buttons())

if __name__ == '__main__':
    executor.start_polling(dp)
