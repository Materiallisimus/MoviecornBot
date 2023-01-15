import telebot

bot = telebot.TeleBot('5630641295:AAG6-wUv8OddI8tYgZxufGoO3zThqc6uu9M')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHQvNjw99Jr1FfbfsX6prMZevV-A-fgwACAQEAAladvQoivp8OuMLmNC0E')
    bot.send_message(message.chat.id, '<b>Привет! Здесь ты сможешь найти понравившийся фильм!</b> Просто отправь код из видео👇', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "100":
        bot.send_message(message.chat.id, "📼Фильм: <b>Мина</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "110":
            bot.send_message(message.chat.id, "📼Фильм: <b>Алладин</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "111":
        bot.send_message(message.chat.id, "📼Фильм: <b>Балерина</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "112":
        bot.send_message(message.chat.id, "📼Фильм: <b>Детективный синдром</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "113":
        bot.send_message(message.chat.id, "📼Фильм: <b>Добытчица</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "114":
        bot.send_message(message.chat.id, "📼Фильм: <b>Классная Катя</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "115":
        bot.send_message(message.chat.id, "📼Фильм: <b>Круэлла</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "116":
        bot.send_message(message.chat.id, "📼Фильм: <b>Нечего терять</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "117":
        bot.send_message(message.chat.id, "📼Фильм: <b>Одарённая</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "118":
        bot.send_message(message.chat.id, "📼Фильм: <b>Преступница Эмили (2022)</b>\nПриятного просмотра!🍿", parse_mode='html')
    elif message.text == "119":
        bot.send_message(message.chat.id, "📼Фильм: <b>Преступница Эмили (2022)</b>\nПриятного просмотра!🍿",parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так", parse_mode='html')

bot.polling(none_stop=True)