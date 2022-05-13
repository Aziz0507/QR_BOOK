import telebot
from telebot import types



bot = telebot.TeleBot('5300762583:AAGztCSk4ytRfofPKloEwFUIt95LY5oHLpE')

class Function:
    def start_button(self,message):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Kitoni QR formatga keltirish')
        itembtn2 = types.KeyboardButton('Bot xaqida')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id,f"{message.from_user.first_name}, iltimos kerakli tugmani bosing",reply_markup=markup)
        