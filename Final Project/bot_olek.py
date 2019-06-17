import re
import markovify
import os

TOKEN = os.environ['TOKEN']

with open('olek.txt', encoding='utf-8') as f:
    train = f.read()
with open('comments.txt', encoding='utf-8') as f:
    train_com = f.read()
train_com_clean = re.sub('\[.+?\]', 'Олег', train_com.replace('\n', ' '))


# In[3]:


m2 = markovify.Text(train + train_com_clean)


# In[128]:


import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def define_gender(name):
    tag = morph.parse(name)[0].tag
    if 'masc' in tag:
        gender = 'm'
    elif 'femn' in tag:
        gender = 'f'
    else:
        gender = 'n'
    return gender
    
    
def generate_excuse(name):
    gender = define_gender(name)
    if gender == 'm':
        excuse = 'Дорогой {}!'.format(name)
    elif gender == 'f':
        excuse = 'Дорогая {}!'.format(name)
    else:
        excuse = 'Дорогое {}!'.format(name)
    for i in range(3):
        try:
            sent = m2.make_sentence().replace('Олег', name)
        except AttributeError:
            pass
        excuse = excuse + ' ' + sent
    return excuse


# ### Создаём бота

# In[141]:


import flask
import telebot
import conf

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

#telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'} #задаем прокси
bot = telebot.TeleBot(TOKEN) #, threaded=False)  # бесплатный аккаунт pythonanywhere запрещает работу с несколькими тредами

# удаляем предыдущие вебхуки, если они были
bot.remove_webhook()

# ставим новый вебхук = Слышь, если кто мне напишет, стукни сюда — url
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)


# In[142]:


bosses = {}

def the_boss(chat_id):
    try:
        boss = bosses[chat_id]
    except KeyError:
        boss = 'Олек'
    return boss

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Дорогой пользователь, к сожалению, проект ещё не готов, но я могу оправдаться и подготовить оправдание для Вас тоже.')
    bot.send_message(message.chat.id, 'Введите /help, чтобы начать работать над вашим проектом... то есть оправданием!')
    
@bot.message_handler(commands = ['help'])
def send_help(message):
    helper = '''Введите /start, чтобы начать.
Введите /help, чтобы получить инструкции.
Введите /excuse, чтобы получить оправдание.
Введите /boss, чтобы проверить имя Вашего босса.
Введите /boss_name, чтобы сменить имя Вашего босса.'''
    bot.send_message(message.chat.id, helper)

@bot.message_handler(commands = ['excuse'])
def send_excuse(message):
    reply = generate_excuse(the_boss(message.chat.id))
    bot.send_message(message.chat.id, reply)

@bot.message_handler(commands = ['boss_name'])
def ask_for_name(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = telebot.types.KeyboardButton('Олек')
    btn2 = telebot.types.KeyboardButton('Не Олек')
    keyboard.add(btn1, btn2)
    sent = bot.send_message(message.chat.id, 'Как зовут Вашего босса?', reply_markup=keyboard)
    bot.register_next_step_handler(sent, work_with_boss_name)
    
def work_with_boss_name(message):
    your_boss = message.text
    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    if your_boss == 'Не Олек':
        question = bot.send_message(message.chat.id, 'Введите имя босса:', reply_markup=markup)
        bot.register_next_step_handler(question, ask_own_name)
    elif your_boss == 'Олек':
        bot.send_message(message.chat.id, 'Мой тоже Олек!', reply_markup=markup)
        bosses[message.chat.id] = 'Олек'
        bot.send_message(message.chat.id, 'У меня есть много оправданий для Олека. Введите /excuse и проверьте сами!')
    else:
        bot.send_message(message.chat.id, 'Чего-то Вы не то делаете. Он либо Олек, либо не Олек. Попробуйте /boss_name ещё разок.', reply_markup=markup)
    
@bot.message_handler(commands = ['boss'])
def send_boss(message):
    bot.send_message(message.chat.id, 'Ваш босс:{}.'.format(the_boss(message.chat.id)))
    bot.send_message(message.chat.id, 'Если это не так, введите /boss_name.')
    
@bot.message_handler(func=lambda message: True)
def default_command(message):
    bot.send_message(message.chat.id, 'Не понимаю.')
    send_help(message)

@bot.message_handler(content_types=['text'])
def ask_own_name(message):
    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    boss = message.text
    try:
        bot.send_message(message.chat.id, boss + '? Знаю таких!', reply_markup=markup)
        bosses[message.chat.id] = boss
        bot.send_message(message.chat.id, 'Введите /excuse и я подготовлю для босса лучшее оправдание!')
    except TypeError:
        bot.send_message(message.chat.id, 'Неа, так не пойдёт. Введите /boss_name и попробуйте ещё раз.')


# In[144]:


#bot.polling(none_stop=True)

# In[ ]:


# пустая главная страничка для проверки
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

# обрабатываем вызовы вебхука = функция, которая запускается, когда к нам постучался телеграм
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

