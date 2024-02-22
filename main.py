# -*- coding: utf-8 -*-
import telebot
import webbrowser
from telebot import types
bot=telebot.TeleBot("6618364860:AAHUKJm1POmTFTfg75DAoW4_OlsltuEwCNw")

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('О компании')
    btn2 = types.KeyboardButton('Записаться на консультацию')
    btn3 = types.KeyboardButton('Об услугах')
    btn4=types.KeyboardButton("Акции")
    markup.row(btn1, btn3)
    markup.add(btn2, btn4)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}!\n\nВас приветствует бухгалтерский центр Дианы Царбаевой! Мы помогаем вашему бизнесу уже более 10 лет и за последний год сэкономили 30 миллионов рублей своим клиентам.\n\nЗдесь Вы можете подробнее узнать о бухгалтерском центре Дианы Царбаевой и предоставляемых услугах, а также записаться на консультацию", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text)
def start_menu(message):
    if message.text=="О компании":
        bot.send_video(message.chat.id, "BAACAgIAAxkBAAIB22XVDMQltWEga_J2EJVV2-Hrw4I5AAIPRQAC5O2pShEXgPZ9uOKNNAQ", caption="✅ <b>У нас более 140 клиентов на обслуживание</b>\n\n✅ <b>Мы сэкономили 30 миллионов рублей за последний год</b>\n\n✅ <b>Имеем 20 лет непрерывного опыта</b>\n\n✅ <b>1000+ консультаций</b>\n\n✅ <b>5000+ решенныйх вопосов</b>\n\n✅ <b>Законно снижаем налоги и уменьшаем расходы вашего бизнеса</b>", parse_mode="HTML")
    elif message.text=="Об услугах":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Бухгалтерские услуги")
        btn2=types.KeyboardButton("Регистрационные действия")
        btn3=types.KeyboardButton("Аудит")
        btn4=types.KeyboardButton("Консультирование")
        btn5=types.KeyboardButton("Разовые услуги")
        btn7=types.KeyboardButton("Вернуться назад")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn7)
        bot.send_message(message.chat.id, "Выберите необходимый тип услуги", reply_markup=markup)
    elif message.text == "Бухгалтерские услуги":
        bot.send_message(message.chat.id,
                         "✅ Полное бухгалтерское обслуживание ООО и ИП\n\n✅ Решаю проблемы с налоговой\n\n✅ Ответы на требования\n\n✅ Кадровый учет\n\n✅ Расчет зарплаты, налогов и взносов\n\n✅ Оформление первичных документов\n\n✅ Составление и сдача отчетности в налоговые органы, внебюджетные фонды, органы стантистики, другие государственные органы")
    elif message.text == "Регистрационные действия":
        bot.send_message(message.chat.id,
                         "✅ Регистрация ООО и ИП, закрытие ООО и ИП\n\n✅ Подбор ОКВЭД\n\n✅ Открытие расчетных счетов, защита")
    elif message.text == "Аудит":
        bot.send_message(message.chat.id, "✅ Восстановление учета\n\n✅ Аудит бухгалтерской базы 1С\n\n")
    elif message.text == "Консультирование":
        bot.send_message(message.chat.id,
                         "✅ Подбор кассы, эквайринга и системы платежей\n\n✅ Консультации по бухгалтерскому и налоговому учету")
    elif message.text == "Разовые услуги":
        bot.send_message(message.chat.id,
                         "✅ Сопровождение налоговых проверок\n\n✅ Контроль и подготовка платежных поручений на уплату налогов, взносов\n\n✅ Любой другой комплекс бухгалтерских услуг")
    elif message.text=="Вернуться назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('О компании')
        btn2 = types.KeyboardButton('Записаться на консультацию')
        btn3 = types.KeyboardButton('Об услугах')
        btn4 = types.KeyboardButton("Акции")
        markup.row(btn1, btn3)
        markup.add(btn2, btn4)
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=markup)
    elif message.text=="Записаться на консультацию":
        m=types.InlineKeyboardMarkup()
        btn6=types.InlineKeyboardButton("Записаться", url="https://t.me/Diana_nalogi")
        m.row(btn6)
        bot.send_message(message.chat.id, "Для записи нажмите кнопку ниже\n\nTelegram канал: https://t.me/diana_nalog\n\nVK: https://vk.com/club73536707\n\nYouTube: https://youtube.com/@DIANA_CZARBAEBA?si=rZOPSh0BtTZN-AC5", reply_markup=m)
    elif message.text=="Акции":
        bot.send_message(message.chat.id, "СОТРУДНИЧЕСТВО\n\nЯ предлагаю вам денежное вознаграждение за рекомендацию меня как специалиста:\n\nВы рекомендуете меня, а при заключении договора с новым клиентом от вас вы получаете  50% оплаты за первый месяц обслуживания лично от меня 🤝\n\nПравила:\n\n1️⃣ Кто-то из ваших знакомых находится в поиске хорошего бухгалтера\n\n2️⃣ Вы даете ему мои контакты\n\n3️⃣ Мы созваниваемся, договариваемся об обслуживании, согласовав стоимость\n\n4️⃣ Как только я получаю оплату за первый месяц обслуживания (например, 10 000 руб.), 50%, то есть 5 000 руб. перевожу вам\n\n‼️ У меня есть специальная форма договора, разработанная юристом, специально для нашего сотрудничества\n\n‼️ Обязательно сообщите, что клиент от вас")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю, попробуйте ещё раз")
# @bot.message_handler(content_types=['video'])
# def f(message):
#     print(message.video.file_id)

# @bot.message_handler(func=lambda message:message.text)
# def services(message):
#     if message.text=="Бухгалтерские услуги":
#         bot.send_message(message.chat.id, "✅ Полное бухгалтерское обслуживание ООО и ИП\n\n✅ Решаю проблемы с налоговой\n\n✅ Ответы на требования\n\n✅ Кадровый учет\n\n✅ Расчет зарплаты, налогов и взносов\n\n✅ Оформление первичных документов\n\n✅ Составление и сдача отчетности в налоговые органы, внебюджетные фонды, органы стантистики, другие государственные органы")
#     elif message.text=="Регистрационные действия":
#         bot.send_message(message.chat.id, "✅ Регистрация ООО и ИП, закрытие ООО и ИП\n\n✅ Подбор ОКВЭД\n\n✅ Открытие расчетных счетов, защита")
#     elif message.text=="Аудит":
#         bot.send_message(message.chat.id, "✅ Восстановление учета\n\n✅ Аудит бухгалтерской базы 1С\n\n")
#     elif message.text=="Консультирование":
#         bot.send_message(message.chat.id, "✅Подбор кассы, эквайринга и системы платежей\n\n✅ Консультации по бухгалтерскому и налоговому учету")
#     elif message.text=="Разовые услуги":
#         bot.send_message(message.chat.id, "✅ Сопровождение налоговых проверок\n\n✅ Контроль и подготовка платежных поручений на уплату налогов, взносов\n\n✅ Любой другой комплекс бухгалтерских услуг")

# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.InlineKeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото')
#     btn3 = types.InlineKeyboardButton('Изменить текст')
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, "Привет", reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, "<u>Help information</u>", parse_mode='html')
# информация об объектах


# @bot.message_handler()
# def info(message):
#     bot.send_message(message.chat.id, message.text)
    # if message.text.lower()=='привет':
    #     bot.send_message(message.chat.id, f"Привет!, {message.from_user.first_name}")
    # elif message.text.lower()=='id':
    #     bot.reply_to(message, f'id: {message.from_user.id}')
# @bot.message_handler(commands=['hello'])
# def main(message):
#     bot.send_message(message.chat.id, f"Привет!, {message.from_user.first_name}")
# def on_click(message):
#     if message.text=='Перейти на сайт':
#         bot.send_message(message.chat.id, "Website is open")
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://vk.com/vane_kurbatov')
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, "Привет!")
#
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup=types.InlineKeyboardMarkup()
#     btn1=types.InlineKeyboardButton('Перейти на сайт', url='https://vk.com/vane_kurbatov')
#     markup.row(btn1)
#     btn2=types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3=types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data=='delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
#     elif callback.data=='edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

#bot.polling(none_stop=True, timeout=2000)
bot.infinity_polling()
