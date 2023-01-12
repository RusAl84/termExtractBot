import telebot
import os
import termExtract as te

# Создаем бота, пишем свой токен
# bot = telebot.TeleBot('Здесь твой токен, полученный от @botfather')
bot = telebot.TeleBot('5982175377:AAH4V5oGT1kmyCKnrLo--w9RHvEJLW7DI9s')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(
        m.chat.id, 'Я на связи. Напиши мне текст из которого нужно извлечь ключевые слова')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = te.term_extract(message.text)
    bot.send_message(message.chat.id, s)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
