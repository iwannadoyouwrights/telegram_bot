# coding: utf-8
import telegram
import random
from urllib.request import urlopen
import re
import json

def dictr():
    pages = ['a', 'b', 'v', 'g', 'd', 'ye', 'zh', 'z', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'e', 'yu', 'ya']
    br = ''
    sq = ''
    t = []
    ended = []
    for grab in pages:
        g = urlopen('http://smogue.com/glossary/%s.php' %grab).read().decode('utf-8')
        if '<br />' in g:
            br = '<br />'
        elif '<br/>' in g:
            br = '<br/>'
        li = re.findall('<span class="orange">(.*)</span>(.*)'+br+br,g)
        for vfg in li:
            t.append(vfg)
    for i in t:
        ended.append(list(i))
    for i in ended:
        i[1] = i[1].replace(' – ','')
        i[1] = i[1].replace(' - ','')
        i[1] = i[1].replace('</em>','')
        i[1] = i[1].replace('<em>','')
        i[1] = i[1].replace('<strong>',' ')
        i[1] = i[1].replace('</strong>',' ')
    return ended


dit = dictr()


updater = telegram.Updater(token='179534327:AAFedcYG-OglD8Mpq6uHb0kSX6RW8yyNDew')
dispatcher = updater.dispatcher


def start_game(bot, update):
    repl = telegram.ReplyKeyboardMarkup([["/1", "/2", "/3"]], one_time_keyboard=True,resize_keyboard=True)
    global random_ans
    global random_words
    random_words = []
    for i in range(3):
        random_words.append(random.choice(dit))
    random_ans = random_words[0]
    bot.sendMessage(chat_id=update.message.chat_id, text=random_ans[0])
    random.shuffle(random_words)
    variants = 1
    for i in random_words:
        if variants != 3:
            bot.sendMessage(chat_id=update.message.chat_id, text='/%d %s'%(variants,i[1]))
            variants+=1
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text='/%d %s'%(variants,i[1]),reply_markup=repl)
        
         








def one(bot, update):
    if random_words[0][1] == random_ans[1]:
        bot.sendMessage(chat_id=update.message.chat_id, text='Привильно')
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='Неправильно')
    
    start_game(bot, update)

     
def two(bot, update):
    if random_words[1][1] == random_ans[1]:
       bot.sendMessage(chat_id=update.message.chat_id, text='Привильно')
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='Неправильно')
        
    start_game(bot, update)

    
def three(bot, update):
    if random_words[2][1] == random_ans[1]:
        bot.sendMessage(chat_id=update.message.chat_id, text='Привильно')
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='Неправильно')
        
    start_game(bot, update)
    
    

dispatcher.addTelegramCommandHandler('start_game',start_game)
dispatcher.addTelegramCommandHandler('1',one)
dispatcher.addTelegramCommandHandler('2',two)
dispatcher.addTelegramCommandHandler('3',three)

updater.start_polling()
