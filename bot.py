import config
import os
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from random import choice

img_name = choice(os.listdir('memer'))

API_TOKEN = config.TG_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['info'])
def send_info(message):
    print(message)
    bot.reply_to(message,"Здесь есть информация о боте" )
    


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    print(message)
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)
    # тест
    
    photo1 = open('memer/a.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo1)

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)


#@bot.command()
#async def mem(ctx):
    #with open(f'images/{img_name}', 'rb') as f:     
    # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        #picture = discord.File(f)
   #Можем передавать файл как параметр!
    #await ctx.send(file=picture)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['photo', 'file', 'voice'])
def memr_photo(message):
    bot.reply_to(message, choice(['aaa','bbb','ccc']))


bot.infinity_polling()

