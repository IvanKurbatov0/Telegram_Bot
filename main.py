# -*- coding: utf-8 -*-
import telebot
import webbrowser
from telebot import types

token="6795127473:AAFMpd71jrUBLKtjsKEexCA4DE36EhM6crw"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('О компании')
    btn2 = types.KeyboardButton('Записаться на консультацию')
    btn3 = types.KeyboardButton('Об услугах')
    btn4=types.KeyboardButton("Акции")
    markup.row(btn1, btn3)
    markup.add(btn2, btn4)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! 👋\n\nВас приветствует бухгалтерский центр Дианы Царбаевой! Мы помогаем вашему бизнесу уже более 20 лет и за последний год сэкономили 30 миллионов рублей своим клиентам.\n\n📍 Здесь Вы можете подробнее узнать о бухгалтерском центре Дианы Царбаевой и предоставляемых услугах, а также записаться на консультацию", reply_markup=markup)

# @bot.message_handler(content_types=['video'])
# def vid(message):
#     id=message.video.file_id
#     print(id)

@bot.message_handler(func=lambda message: message.text)
def start_menu(message):
    if message.text.lower()=="о компании":
        bot.send_video(message.chat.id, "BAACAgIAAxkBAAMIZerNKraOgoJlEuco-NI4dOCrQ6kAAgFAAALQlllLobeJmKC6V480BA", caption="✅ <b>У нас более 140 клиентов на обслуживание</b>\n\n✅ <b>Мы сэкономили 30 миллионов рублей за последний год</b>\n\n✅ <b>Имеем 20 лет непрерывного опыта</b>\n\n✅ <b>1000+ консультаций</b>\n\n✅ <b>5000+ решённых вопрсов</b>\n\n✅ <b>Законно снижаем налоги и уменьшаем расходы вашего бизнеса</b>", parse_mode="HTML")
    elif message.text.lower()=="об услугах":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Бухгалтерские услуги")
        btn2=types.KeyboardButton("Регистрационные действия")
        btn3=types.KeyboardButton("Аудит")
        btn4=types.KeyboardButton("Консультирование")
        btn5=types.KeyboardButton("Разовые услуги")
        btn7=types.KeyboardButton("⬅️ Вернуться назад")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn7)
        bot.send_message(message.chat.id, "Выберите необходимый тип услуги", reply_markup=markup)
    elif message.text.lower() == "бухгалтерские услуги":
        bot.send_message(message.chat.id,
                         "✅ Полное бухгалтерское обслуживание ООО и ИП\n\n✅ Решаем проблемы с налоговой\n\n✅ Ответы на требования\n\n✅ Кадровый учет\n\n✅ Расчет зарплаты, налогов и взносов\n\n✅ Оформление первичных документов\n\n✅ Составление и сдача отчетности в налоговые органы, внебюджетные фонды, органы стантистики, другие государственные органы")
    elif message.text.lower() == "регистрационные действия":
        bot.send_message(message.chat.id,
                         "✅ Регистрация ООО и ИП\n\n✅ Закрытие ИП\n\n✅ Ликвидация ООО\n\n✅ Подбор ОКВЭД\n\n✅ Открытие расчетных счетов, зашита")
    elif message.text.lower() == "аудит":
        bot.send_message(message.chat.id, "✅ Восстановление учета\n\n✅ Аудит бухгалтерской базы 1С\n\n")
    elif message.text.lower() == "консультирование":
        bot.send_message(message.chat.id,
                         "✅ Подбор кассы, эквайринга и системы платежей\n\n✅ Консультации по бухгалтерскому и налоговому учету\n\n✅ Консультации по подбору правильной системы налогообложения\n\n✅ Консультации по оформлению сотрудников")
    elif message.text.lower() == "разовые услуги":
        bot.send_message(message.chat.id,
                         "✅ Сопровождение налоговых проверок\n\n✅ Контроль и подготовка платежных поручений на уплату налогов, взносов\n\n✅ Любой другой комплекс бухгалтерских услуг")
    elif message.text.lower()=="⬅️ вернуться назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('О компании')
        btn2 = types.KeyboardButton('Записаться на консультацию')
        btn3 = types.KeyboardButton('Об услугах')
        btn4 = types.KeyboardButton("Сотрудничество")
        markup.row(btn1, btn3)
        markup.add(btn2, btn4)
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=markup)
    elif message.text.lower()=="записаться на консультацию":
        m=types.InlineKeyboardMarkup()
        btn6=types.InlineKeyboardButton("Записаться", url="https://t.me/Diana_nalogi")
        m.row(btn6)
        bot.send_message(message.chat.id, "Для записи нажмите кнопку ниже\n\nTelegram канал: https://t.me/diana_nalog\n\nVK: https://vk.com/club73536707\n\nYouTube: https://youtube.com/@DIANA_CZARBAEBA?si=rZOPSh0BtTZN-AC5", reply_markup=m)
    elif message.text.lower()=="сотрудничество":
        bot.send_message(message.chat.id, "✨ СОТРУДНИЧЕСТВО ✨\n\nЯ предлагаю вам денежное вознаграждение за рекомендацию меня как специалиста:\n\nВы рекомендуете меня, а при заключении договора с новым клиентом от вас вы получаете  50% оплаты за первый месяц обслуживания лично от меня 🤝\n\nПравила:\n\n1️⃣ Кто-то из ваших знакомых находится в поиске хорошего бухгалтера\n\n2️⃣ Вы даете ему мои контакты\n\n3️⃣ Мы созваниваемся, договариваемся об обслуживании, согласовав стоимость\n\n4️⃣ Как только я получаю оплату за первый месяц обслуживания (например, 10 000 руб.), 50%, то есть 5 000 руб. перевожу вам\n\n‼️ У меня есть специальная форма договора, разработанная юристом, специально для нашего сотрудничества\n\n‼️ Обязательно сообщите, что клиент от вас")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю, попробуйте ещё раз")


bot.polling(none_stop=True, timeout=2000)
