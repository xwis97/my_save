import serial
import telebot
import requests

ser = serial.Serial("COM11")
ser.baudrate = 115200

bot = telebot.TeleBot('5286624058:AAEWfD4jtFuBmeekKQWcDi_hwIBSTRv_qcA')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, '1' + message.text)
    print (message.text)
    ser.write(message.text.encode('utf-8'))

# Запускаем бота
bot.polling(none_stop=True, interval=0)

