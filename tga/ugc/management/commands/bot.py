from abc import ABC

from aiogram.utils import executor
from django.core.management.base import BaseCommand


from ugc.management.commands.text import text1, text2, text3, text5, text7, text6, text8, text9, text10, text11, \
    text12, text13, text14, \
    text15, text16, text17, text18, text19, text20, text21, text22, text4, text23, text24

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token='1396506839:AAGC8G-3J_4xHHcYZsyuw-uha8zTvpZ68yc')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(text2, reply_markup=markup1)


# Кнопки после старта
new_button1 = KeyboardButton('Начать')
new_button2 = KeyboardButton('Партнерам')
new_button3 = KeyboardButton('Помощь')


@dp.message_handler(text='Начать')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup2)


@dp.message_handler(text='Партнерам')
async def new_1(message: types.Message):
    await message.reply('🤝 Уважаемый партнер! Вероятно. у Вас накопились вопросы ❓\n\
Тогда поищи ответы здесь 👇', reply_markup=markup3)


@dp.message_handler(text='Помощь')
async def new_1(message: types.Message):
    await message.reply('❓ ❓❓ Остались вопросы? Нужна помощь в активации смарт-контракта?\n\
                        Обратитесь с вопросом менеджеру, либо пишите в общий чат, где вам обязательно помогут.'
                        , reply_markup=markup4)




markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row(new_button1).row(new_button2, new_button3)


# Кнопки "Начать"
start_buttons1 = KeyboardButton('Активировать')
start_buttons2 = KeyboardButton('Доходность')
start_buttons3 = KeyboardButton('О проекте FairPact')
start_buttons4 = KeyboardButton('_НАЗАД_')


@dp.message_handler(text='Активировать')
async def new_1(message: types.Message):
    await message.reply(text3, reply_markup=markup5)


@dp.message_handler(text='Доходность')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup6)


@dp.message_handler(text='О проекте FairPact')
async def new_1(message: types.Message):
    await message.reply(text12, reply_markup=markup7)


@dp.message_handler(text='_НАЗАД_')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup1)



markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(start_buttons1, start_buttons2).row(start_buttons3,
                                                                                            start_buttons4)


# Кнопки "Паркнерам"
for_partners_buttons1 = KeyboardButton('О компании WERCA')
for_partners_buttons2 = KeyboardButton('Ваш ID')
for_partners_buttons3 = KeyboardButton('_НАЗАД')


@dp.message_handler(text='О компании WERCA')
async def new_1(message: types.Message):
    await message.reply(text19, reply_markup=markup12)


@dp.message_handler(text='Ваш ID')
async def new_1(message: types.Message):
    await message.reply(text13, reply_markup=markup13)


@dp.message_handler(text='_НАЗАД')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup1)

markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(for_partners_buttons1,
                                                        for_partners_buttons2).row(for_partners_buttons3)
# Кнопки "Помощь"
help_buttons1 = KeyboardButton('Задать вопрос')
help_buttons2 = KeyboardButton('Контакты')
help_buttons3 = KeyboardButton('Назад_')


@dp.message_handler(text='Задать вопрос')
async def new_1(message: types.Message):
    await message.reply('❗️ Ждем Вашего вопроса. Напиши, и мы ответим 👇 @bot_questions_fairpact_bot')


@dp.message_handler(text='Контакты')
async def new_1(message: types.Message):
    await message.reply('👉В общем чате Вам помогут с активацией смарт-контракта и проконсультируют по любым вопросам')


@dp.message_handler(text='Назад_')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup1)


markup4 = ReplyKeyboardMarkup(resize_keyboard=True).row(help_buttons1, help_buttons2).row(help_buttons3)

# Кнопки   "Активировать"
activate_buttons1 = KeyboardButton('Установить')
activate_buttons2 = KeyboardButton('Купить ETH')
activate_buttons3 = KeyboardButton('Вызов смарт-контракта')
activate_buttons4 = KeyboardButton('Назад.')


@dp.message_handler(text='Установить')
async def new_1(message: types.Message):
    await message.reply(text23, reply_markup=markup8)


@dp.message_handler(text='Купить ETH')
async def new_1(message: types.Message):
    await message.reply(text5)


@dp.message_handler(text='Вызов смарт-контракта')
async def new_1(message: types.Message):
    await message.reply(text6, reply_markup=markup9)


@dp.message_handler(text='Назад.')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup2)

markup5 = ReplyKeyboardMarkup(resize_keyboard=True).add(activate_buttons1, activate_buttons2).row(activate_buttons3,
                                                                                                  activate_buttons4)

# Кнопки "Доходность"
profitability_buttons1 = KeyboardButton('Маркетинг')
profitability_buttons2 = KeyboardButton('Бонусная программа')
profitability_buttons3 = KeyboardButton('*-Назад')


@dp.message_handler(text='Маркетинг')
async def new_1(message: types.Message):
    await message.reply(text24, reply_markup=markup10)


@dp.message_handler(text='Бонусная программа')
async def new_1(message: types.Message):
    await message.reply(text13, reply_markup=markup11)


@dp.message_handler(text='*-Назад')
async def new_1(message: types.Message):
    await message.reply('ok', reply_markup=markup2)

markup6 = ReplyKeyboardMarkup(resize_keyboard=True).row(profitability_buttons1,
                                                        profitability_buttons2).row(profitability_buttons3)
# Кнопки "О проекте FairPact"
about_FairPact1 = KeyboardButton('О смарт-контракте')
about_FairPact2 = KeyboardButton('О маркетинге')
about_FairPact3 = KeyboardButton('О блокчейне')
about_FairPact4 = KeyboardButton('О создателе')
about_FairPact5 = KeyboardButton('Назад:')


@dp.message_handler(text='О смарт-контракте')
async def new_1(message: types.Message):
    await message.reply(text9)


@dp.message_handler(text='О маркетинге')
async def new_1(message: types.Message):
    await message.reply(text11)


@dp.message_handler(text='О блокчейне')
async def new_1(message: types.Message):
    await message.reply(text10)


@dp.message_handler(text='О создателе')
async def new_1(message: types.Message):
    await message.reply(text18)


@dp.message_handler(text='Назад:')
async def new_1(message: types.Message):
    await message.reply('ok', reply_markup=markup2)


markup7 = ReplyKeyboardMarkup(resize_keyboard=True).row(about_FairPact1, about_FairPact2).row(about_FairPact3,
                                                                                              about_FairPact4).row(about_FairPact5)

# Кнопки "установить"

install_1 = KeyboardButton('На пк')
install_2 = KeyboardButton('На телефоне')
install_3 = KeyboardButton('- Назад')


@dp.message_handler(text='На пк')
async def new_1(message: types.Message):
    await message.reply(text7)


@dp.message_handler(text='На телефоне')
async def new_1(message: types.Message):
    await message.reply(text4)


@dp.message_handler(text='- Назад')
async def new_1(message: types.Message):
    await message.reply('ok', reply_markup=markup5)

markup8 = ReplyKeyboardMarkup(resize_keyboard=True).row(install_1, install_2).row(install_3)

# Кнопки "Вызов смарт-контракта"

Calling_a_smart_contract_1 = KeyboardButton('На ПК (Metamask)')
Calling_a_smart_contract_2 = KeyboardButton('На телефоне (Android, IOS)')
Calling_a_smart_contract_3 = KeyboardButton('=-назад')


@dp.message_handler(text='На ПК (Metamask)')
async def new_1(message: types.Message):
    await message.reply(text7)


@dp.message_handler(text='На телефоне (Android, IOS)')
async def new_1(message: types.Message):
    await message.reply(text8)


@dp.message_handler(text='=-назад')
async def new_1(message: types.Message):
    await message.reply("ок", reply_markup=markup5)

markup9 = ReplyKeyboardMarkup(resize_keyboard=True).row(Calling_a_smart_contract_1,
                                                        Calling_a_smart_contract_2).row(Calling_a_smart_contract_1)

# Кнопки "Маркетинг"

Marketing_1 = KeyboardButton('1 уровень')
Marketing_2 = KeyboardButton('2 уровень')
Marketing_3 = KeyboardButton('3 уровень')
Marketing_4 = KeyboardButton('4 уровень')
Marketing_5 = KeyboardButton('^НАЗАД')


@dp.message_handler(text='1 уровень')
async def new_1(message: types.Message):
    await message.reply('1️⃣ УРОВЕНЬ'
                        '✅ Стоимость – 0.2 ETH\n\
✅ Прибыль от продажи первого уровня – 0.32 ETH\n\
✅ Кол-во партнеров – 2 человека')


@dp.message_handler(text='2 уровень')
async def new_1(message: types.Message):
    await message.reply('2️⃣ УРОВЕНЬ\n\
✅ Стоимость – 0.3 ETH\n\
✅ Прибыль от продажи второго уровня – 0.96 ETH\n\
✅ Кол-во партнеров – 4 человека')


@dp.message_handler(text='3 уровень')
async def new_1(message: types.Message):
    await message.reply('3️⃣ УРОВЕНЬ\n\
\n\
✅ Стоимость  – 0.5 ETH\n\
✅ Прибыль от продажи третьего уровня – 3.2 ETH\n\
✅ Кол-во партнеров - 8 человек')


@dp.message_handler(text='4 уровень')
async def new_1(message: types.Message):
    await message.reply('4️⃣ УРОВЕНЬ\n\
✅ Стоимость входа – 1 ETH\n\
✅ Прибыль от продажи четвертого уровня – 12.8 ETH\n\
✅ Кол-во партнеров - 16 человек')


@dp.message_handler(text='^НАЗАД')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup6)


markup10 = ReplyKeyboardMarkup(resize_keyboard=True).row(Marketing_1, Marketing_2).row(Marketing_3,
                                                                                      Marketing_4).row(Marketing_5)


# Кнопки "Бонусная программа"

bonus_program_1 = KeyboardButton('от 15%')
bonus_program_2 = KeyboardButton('от 20%')
bonus_program_3 = KeyboardButton('от 25%')
bonus_program_4 = KeyboardButton('от 30%')
bonus_program_5 = KeyboardButton('назад-*')


@dp.message_handler(text='от 15%')
async def new_1(message: types.Message):
    await message.reply(text14)


@dp.message_handler(text='от 20%')
async def new_1(message: types.Message):
    await message.reply(text15)


@dp.message_handler(text='от 25%')
async def new_1(message: types.Message):
    await message.reply(text16)


@dp.message_handler(text='от 30%')
async def new_1(message: types.Message):
    await message.reply(text17)


@dp.message_handler(text='назад-*')
async def new_1(message: types.Message):
    await message.reply('ок', reply_markup=markup6)

markup11 = ReplyKeyboardMarkup(resize_keyboard=True).row(bonus_program_1, bonus_program_2).row(bonus_program_3,
                                                                                               bonus_program_4).row(bonus_program_5)

#  Кнопки "Ваш ID"

id_1 = KeyboardButton('Как найти свой ID в структуре?')
id_2 = KeyboardButton('Как проходит покупка следующего уровня?')
id_3 = KeyboardButton('Почему')
id_4 = KeyboardButton('Что')
id_5 = KeyboardButton('Где')
id_6 = KeyboardButton('Когда')
id_7 = KeyboardButton('Назад!')

markup13 = ReplyKeyboardMarkup(resize_keyboard=True).row(id_1, id_2).row(id_3, id_4).row(id_5, id_6).row(id_7)



@dp.message_handler(text='Как найти свой ID в структуре?')
async def new_1(message: types.Message):
    await message.reply('Как найти свой ID в структуре\n\
1.Переходите по ссылке 👉 https://fairpact.ru/structure/\n\
 2. Кликаете слева вверху на "CHANGE ID"\n\
 3. В поле вбиваете 1685 - центральный ID ветки')


@dp.message_handler(text='Как проходит покупка следующего уровня?')
async def new_1(message: types.Message):
    await message.reply('text')


@dp.message_handler(text='Почему')
async def new_1(message: types.Message):
    await message.reply('🔹Почему я не могу найти свой ID на структуре ❓\n\
\n\
🔸 По всей вероятности, из-за большого количества партнеров и небольшого размера схемы. Но есть выход:\n\
👉 Закройте одну из веток ID 1689 слева и ID 1690 справа от Вас.  Схема станет больше. Попробуйте свернуть несколько «ног", и станет еще больше и лучше видна.')


@dp.message_handler(text='Что')
async def new_1(message: types.Message):
    await message.reply('🔹 Что произойдет, если я не куплю уровень ❓\n\
\n\
🔸 Тогда деньги, которые Вы должны были бы получить от своих партнеров,  уйдут выше. Однако, это не значит, что вы совсем потеряли свою прибыль. Быстрее повышайте уровень, и остальные переливы вновь будут поступать к Вам.\n\
\n\
❗️Очень важно быть подключенным к чату в Telegram, чтобы не пропустить новости, в том числе и о поднятии уровней.\n\
👉Для присоединения зайдите в раздел КОНТАКТЫ')


@dp.message_handler(text='Где')
async def new_1(message: types.Message):
    await message.reply('🔹 Где я могу посмотреть, есть ли партнеры под моим ID ❓\n\
🔸 Вы можете посмотреть свою структуру на сайте проекта по адресу 👉 https://fairpact.ru/structure/')


@dp.message_handler(text='Когда')
async def new_1(message: types.Message):
    await message.reply('🔹Когда необходимо поднимать уровень? Как я об этом узнаю ❓\n\
🔸Согласно нашей стратегии, уровни поднимаются одновременно всеми партнерами в ряду. О необходимости поднять уровень Вам сообщат менеджеры нашего проекта.\n\
❗️Важно быть участником основного Тelеgram канала и следить за сообщениями от менеджеров проекта. \n\
👉Проверьте, подписаны ли Вы на канал? Для этого зайдите  в раздел КОНТАКТЫ')


@dp.message_handler(text='Назад!')
async def new_1(message: types.Message):
    await message.reply(text1, reply_markup=markup3)


# Кнопки "О компании WERCA"

werca_1 = KeyboardButton('Наши проекты')
werca_2 = KeyboardButton('Работа')
werca_3 = KeyboardButton('Команда')
werca_4 = KeyboardButton('Наши соцсети')
werca_5 = KeyboardButton('*Назад*')


markup12 = ReplyKeyboardMarkup(resize_keyboard=True).row(werca_1, werca_2).row(werca_3, werca_4).row(werca_5)


@dp.message_handler(text='Наши проекты')
async def new_1(message: types.Message):
    await message.reply(text20)


@dp.message_handler(text='Работа')
async def new_1(message: types.Message):
    await message.reply(text21)


@dp.message_handler(text='Команда')
async def new_1(message: types.Message):
    await message.reply(text22)


@dp.message_handler(text='Наши соцсети')
async def new_1(message: types.Message):
    await message.reply(text22)


@dp.message_handler(text='*Назад*')
async def new_1(message: types.Message):
    await message.reply('ok', reply_markup=markup3)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(dp)
