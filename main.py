from itertools import chain
import telebot
from telebot import types
from func import bot, Function


func = Function()




@bot.message_handler(commands=['start'])
def Start_handler(message):
    bot.send_message(message.chat.id, 'Salom bu botga xush kelibsiz')
    func.start_button(message)
    
    #print(message.from_user)
@bot.message_handler(content_types=['text'])
def text_leading(message):
    if message.text == 'Kitoni QR formatga keltirish':
        bot.reply_to(message.chat.id, 'ultimos kitobingizni kiriting')
    elif message.text == 'Bot xaqida':
        bot.send_message(message.chat.id, "Bu bot kitobni, pdf formatdan QR kod ko'rinishiga olib keladi")
    else:
        bot.reply_to(message.chat.id, '*_*\nSizni tushunmadim')

@bot.message_handler(content_types=['document'])
def oppgrade_doc(message):
    bot.send_message(message.chat.id, "Bu documentiz yaqin orada QR bo'lib keladi")










bot.infinity_polling()