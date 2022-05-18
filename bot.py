 
import logging
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import settings
import ephem
from datetime import date


logging.basicConfig(filename='bot.log', level=logging.INFO)

# PROXY = {'proxy_url': settings.PROXY_URL,
# 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    # # print(1/0)
    # print(update)  
    # print('*****')
    # print(update.from.)
    update.message.reply_text("Привет, пользователь! Ты вызвал команду /start")

def where_planet(name_planet):
    current_date = str(date.today()).replace('-','/')
  
    try:
        if name_planet.upper() == 'MARS':
            return ephem.constellation(ephem.Mars(current_date))
        elif name_planet.lower() == 'earth':
            return ephem.constellation(ephem.Earth(current_date))
        else:
            return 'Не обрабатываем такую планету'
    except:
        return "Не могу определить планету"
    


def planet_user(update, context):
    name_planet = update.message.text.split()[1]
    update.message.reply_text(where_planet(name_planet))

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    # mybot = Updater("settings.API_KEY", use_context=True, request_kwargs=PROXY)
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()
