from telebot import TeleBot, types

TOKEN = "7445114497:AAF_wsz3YizU3muzNh3tRe1GomphO1hdhOk"
bot = TeleBot(TOKEN)

channel_id = '-1002071497608'

# Inline keyboard for channel subscription
def inline_buttons():
    markup = types.InlineKeyboardMarkup()
    channel_url = types.InlineKeyboardButton("Kanalga o'tish", url='https://t.me/munisa_onlinesavdo_wechat')
    markup.add(channel_url)
    return markup

# Reply keyboard for subscribed users (1 button per row)
buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons.add(
    types.KeyboardButton("Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍")
)
buttons.add(
    types.KeyboardButton("Kurs haqida ma'lumot💠")
)
buttons.add(
    types.KeyboardButton("Kanalimiz⚡️")
)

# Back button keyboard
back_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button.add(types.KeyboardButton("Orqaga qaytish🔙"))

# Function to check subscription
def check_subscription(user_id):
    try:
        member = bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status != 'left'
    except:
        return False

# /start handler
@bot.message_handler(commands=["start"])
def start(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        bot.send_message(message.chat.id, "Siz kanalga a'zo bo'lgansiz☺️", reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, "Assalomu alaykum! Botdan foydalanish uchun iltimos kanalga a'zo bo'ling va /start ni bosing🙃", reply_markup=inline_buttons())

# Buyurtma berish handler
@bot.message_handler(func=lambda message: message.text == "Buyurtma berish yuzasidan bepul foydali ma'lumotlar😍🛍")
def order_info(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("🇨🇳Xitoy davlatidan tovar buyurtma qilishning 5 ta foydali tomoni")
        )
        markup.add(
            types.KeyboardButton("🇹🇷Turkiya davlatidan tovar buyurtma qilishning 3 ta foydali tomoni")
        )
        markup.add(
            types.KeyboardButton("💥iHerb dasturi orqali chegirmalardan foydalanish")
        )
        markup.add(
            types.KeyboardButton("🛂Bojxona haqida")
        )
        markup.add(
            types.KeyboardButton("💠Mustaqil buyurtma berish")
        )
        markup.add(
            types.KeyboardButton("🏘Uyda o`tirgan holda daromad")
        )
        markup.add(types.KeyboardButton("Orqaga qaytish🔙"))
        bot.send_message(message.chat.id, "Davlatni tanlang:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Botdan foydalanish uchun iltimos kanalga a'zo bo'ling", reply_markup=inline_buttons())

# Info messages
def forward_message(chat_id, message_id, target_chat_id):
    try:
        bot.forward_message(chat_id=chat_id, from_chat_id=target_chat_id, message_id=message_id)
    except Exception as e:
        print(f"Error: {e}")

@bot.message_handler(func=lambda message: message.text == "🇨🇳Xitoy davlatidan tovar buyurtma qilishning 5 ta foydali tomoni")
def china_info(message):
    forward_message(message.chat.id, 112, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@bot.message_handler(func=lambda message: message.text == "🇹🇷Turkiya davlatidan tovar buyurtma qilishning 3 ta foydali tomoni")
def turkey_info(message):
    forward_message(message.chat.id, 217, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@bot.message_handler(func=lambda message: message.text == "💥iHerb dasturi orqali chegirmalardan foydalanish")
def iherb_info(message):
    forward_message(message.chat.id, 52, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@bot.message_handler(func=lambda message: message.text == "🛂Bojxona haqida")
def customs_info(message):
    forward_message(message.chat.id, 279, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@bot.message_handler(func=lambda message: message.text == "💠Mustaqil buyurtma berish")
def independent_order_info(message):
    forward_message(message.chat.id, 292, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

@bot.message_handler(func=lambda message: message.text == "🏘Uyda o`tirgan holda daromad")
def home_income_info(message):
    forward_message(message.chat.id, 314, '@munisa_onlinesavdo_wechat')
    bot.send_message(message.chat.id, "Orqaga qaytish uchun tugmani bosing.", reply_markup=back_button)

# Kurs haqida ma'lumot handler
@bot.message_handler(func=lambda message: message.text == "Kurs haqida ma'lumot💠")
def course_info(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        posts = [
            "https://t.me/munisa_onlinesavdo_wechat/436",
            "https://t.me/munisa_onlinesavdo_wechat/437",
            "https://t.me/munisa_onlinesavdo_wechat/438"
        ]
        response = "\n".join(posts)
        bot.send_message(message.chat.id, response, reply_markup=back_button)
    else:
        bot.send_message(message.chat.id, "Botdan foydalanish uchun iltimos kanalga a'zo bo'ling", reply_markup=inline_buttons())

# Kanalimiz handler
@bot.message_handler(func=lambda message: message.text == "Kanalimiz⚡️")
def channel_info(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        bot.send_message(message.chat.id, "Telegram kanal:", reply_markup=inline_buttons())
    else:
        bot.send_message(message.chat.id, "Botdan foydalanish uchun iltimos kanalga a'zo bo'ling", reply_markup=inline_buttons())

# Orqaga qaytish handler
@bot.message_handler(func=lambda message: message.text == "Orqaga qaytish🔙")
def go_back(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        bot.send_message(message.chat.id, "Bosh sahifaga qaytdingiz", reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, "Botdan foydalanish uchun iltimos kanalga a'zo bo'ling", reply_markup=inline_buttons())

# Other messages handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    is_subscribed = check_subscription(message.from_user.id)

    if is_subscribed:
        bot.send_message(message.chat.id, "Siz kanalga a'zo bo'lgansiz. Tugmalarni ishlatishingiz mumkin.", reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, "Botdan foydalanish uchun iltimos kanalga a'zo bo'ling", reply_markup=inline_buttons())

# Botni ishlatish
bot.polling()
