from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext
from telegram import ReplyKeyboardRemove
from telegram.utils.request import Request
from telegram import Bot
from datetime import datetime
import random
from covid import Covid19
from course import Dollar, Hryvnia, Euro, Pound, Yuan, Bitcoin

TOKEN = "1241624025:AAHVYH5uaUnPhEbUhPJCQLoQ8cjUxGzUYd8"

#buttons
button_help = "Помощь"
button_date = "Дата и время"
button_covid = "Статистика COVID-19"
button_covid_world = "По миру"
button_covid_russia = "По России"
button_covid_usa = "По США"
button_covid_dif = "Другая страна.."
button_currency = "Курсы валют"
button_dollar = "Доллар"
button_hryvnia = "Гривна"
button_euro = "Евро"
button_pound = "Пунд Стерлингов"
button_yuan = "Юань"
button_bitcoin = "Биткоин"
button_back = "Назад"

meetings = ["hello", "hi", "buenos dias", "buenos tardes", "привет", "здравствуй"]
#covid_info = open("data/text/covid19.txt", "r").read().replace('?', '/')
covid_info = open("data/text/covid19.txt", "r").read()
help = open("data/text/rules.txt", "r").read()
replics = ["Сегодня все волки всборе и готовы тебе помогать..",
           "Уже заранее пытаюсь найти информацию, чтобы тебе не пришлось ждать",
           "Сегодня должно произойти много интересного",
           "Мой третий глаз меня не подводит",
           "Настало время направить свет на неясность..",
           "Не тот волк - кто не волк, а тот волк - кто волк",
           "Ты уже узнал сколько больных вирусом в России?",
           "Курс Биткоина снова скачет..",
           "Как думаешь, доллар пробьет новый потолок7"]


def main_covid_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_covid_russia),
                KeyboardButton(text=button_covid_usa),
            ],
            [
                KeyboardButton(text=button_covid_world),
                KeyboardButton(text=button_covid_dif),
            ],
            [
              KeyboardButton(text=button_back),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text="Выберите любой инструмент..",
        reply_markup=reply_markup,
    )

def covid_handler(update: Update, context: CallbackContext, tool):
    value = ''
    if tool == button_covid_world:
        covid = Covid19()
        value = covid.check_in_the_world()
    if tool == button_covid_russia:
        covid = Covid19()
        value = covid.check_in_the_russia()
    if tool == button_covid_usa:
        covid = Covid19()
        value = covid.check_in_the_usa()
    if tool == button_covid_dif:
        value = covid_info
    if tool[0] == '?':
        covid = Covid19()
        value = covid.covid_in_different_country(tool)
    if value == 1:
        value = "Врачи пока не могут поделиться информацией.."
    update.message.reply_text(
        text=value,
    )



def choisen_currency(update: Update, context: CallbackContext, currency):
    value = ''
    if currency == button_dollar:
        dollar = Dollar()
        value = dollar.get_currency_price()
    if currency == button_hryvnia:
        hryvnia = Hryvnia()
        value = hryvnia.get_currency_price()
    if currency == button_euro:
        euro = Euro()
        value = euro.get_currency_price()
    if currency == button_pound:
        pound = Pound()
        value = pound.get_currency_price()
    if currency == button_yuan:
        yuan = Yuan()
        value = yuan.get_currency_price()
    if currency == button_bitcoin:
        bitcoin = Bitcoin()
        value = bitcoin.get_currency_price()
    update.message.reply_text(
        text=value,
    )


def meeting_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Привет, я Волчара - бот который не выступает в цирке\nВыберай любую опцию.."
    )


def currency_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_dollar),
                KeyboardButton(text=button_euro),
                KeyboardButton(text=button_pound),
            ],
            [
                KeyboardButton(text=button_yuan),
                KeyboardButton(text=button_hryvnia),
                KeyboardButton(text=button_bitcoin),
            ],
            [
              KeyboardButton(text=button_back)
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text="Выбери любую валюту или крипту..",
        reply_markup=reply_markup,
    )



def date_handler(update: Update, context: CallbackContext):
    now = datetime.now()
    time = str(now.time()).split('.')[0]
    date = str(now.date()).replace('-', '/')
    value = f'Сегодня: {date}\nТочное время: {time}'
    update.message.reply_text(
        text=value
    )


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=help,
        #reply_markup=ReplyKeyboardRemove(),
    )


def start(update: Update, context: CallbackContext):
           reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_date),
                KeyboardButton(text=button_currency),
            ],
            [
                KeyboardButton(text=button_covid),
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text=replics[random.randrange(5)],
        reply_markup=reply_markup,
    )
           
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)
    if text == button_date:
        return date_handler(update=update, context=context)
    if text.lower() in meetings:
        return meeting_handler(update=update, context=context)
    if text == button_currency:
        return currency_handler(update=update, context=context)
    if text == button_dollar:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_hryvnia:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_euro:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_pound:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_yuan:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_bitcoin:
        return choisen_currency(update=update, context=context, currency=text)
    if text == button_covid:
        return main_covid_handler(update=update, context=context)
    if text == button_covid_russia:
        return covid_handler(update=update, context=context, tool=text)
    if text == button_covid_usa:
        return covid_handler(update=update, context=context, tool=text)
    if text == button_covid_world:
        return covid_handler(update=update, context=context, tool=text)
    if text == button_covid_dif:
        return covid_handler(update=update, context=context, tool=text)
    if text[0] == "?":
        return covid_handler(update=update, context=context, tool=text)
    if text.lower() == "назад":
        return start(update=update, context=context)             

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_date),
                KeyboardButton(text=button_currency),
            ],
            [
                KeyboardButton(text=button_covid),
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text=replics[random.randrange(5)],
        reply_markup=reply_markup,
    )


def main():
    req = Request(
        connect_timeout=0.5,
    )
    bot = Bot(
        request=req,
        token=TOKEN,

    )
    updater = Updater(bot=bot, use_context=True)
    print(updater.bot.get_me())
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
