import telebot
import random
import qrcode
import sys
from gtts import gTTS
bot = telebot.TeleBot("2125911362:AAGIRV6lphNHrEU2GxRjB5c2Lus8b9SUdAc")

@bot.message_handler(commands=['start'])  #decorator
def welcome(message):
  username=message.from_user.first_name
  bot.reply_to(message, username+" Hello, Welcome to this bot....How can i help you?")
  markup = telebot.types.ReplyKeyboardMarkup()
  choose1=telebot.types.KeyboardButton("/start")
  choose2=telebot.types.KeyboardButton("/help")
  choose3=telebot.types.KeyboardButton("/age")
  choose4=telebot.types.KeyboardButton("/voice")
  choose5=telebot.types.KeyboardButton("/max")
  choose6=telebot.types.KeyboardButton("/argmax")
  choose7=telebot.types.KeyboardButton("/qrcode")
  choose8=telebot.types.KeyboardButton("/game")
  markup.row(choose1,choose2)
  #markup.add(choose2)
  markup.row(choose3,choose4,choose5)
  #markup.add(choose4)
  #markup.add(choose5)
  markup.row(choose6,choose7,choose8)
  #markup.add(choose7)
  #markup.add(choose8)
  bot.send_message(message.chat.id,"Which Command You want to try?", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "/start\nWelcome\n/game\nGuess number game\n/age\nCalculate your age\n/voice\nChange text into voice\n/max\nfind the biggest number in array\n/argmax\nfind the index of biggest number in array\n/qrcode\nsend a text and take its QRcode\n")
 

@bot.message_handler(commands=['game'])  #decorator
def get_num(message):  
  global com
  com=random.randrange(100)
  user=bot.reply_to(message,"Enter number: ")
  bot.register_next_step_handler(user,Game)
def Game(message):
  global com
  markup = telebot.types.ReplyKeyboardMarkup(selective=False)
  choose=telebot.types.KeyboardButton("New Game")
  markup.add(choose)
  bot.send_message(message.chat.id,"If you want to start a new game,Press (New Game)", reply_markup=markup)
  if(message.text=="New Game"):
    user1=bot.reply_to(message,"Enter your guess: ")
    com=random.randint(0,100)
    bot.register_next_step_handler(user1,Game)
  else:
    
    username=message.text
    username=int(username)
    if(com==username):
      com=str(com)
      bot.reply_to(message,"CONGRATULATIONS!!!\nThe number is "+com)
      markup = telebot.types.ReplyKeyboardMarkup()
      choose1=telebot.types.KeyboardButton("/start")
      choose2=telebot.types.KeyboardButton("/help")
      choose3=telebot.types.KeyboardButton("/age")
      choose4=telebot.types.KeyboardButton("/voice")
      choose5=telebot.types.KeyboardButton("/max")
      choose6=telebot.types.KeyboardButton("/argmax")
      choose7=telebot.types.KeyboardButton("/qrcode")
      choose8=telebot.types.KeyboardButton("/game")
      markup.row(choose1,choose2)
  #markup.add(choose2)
      markup.row(choose3,choose4,choose5)
  #markup.add(choose4)
  #markup.add(choose5)
      markup.row(choose6,choose7,choose8)
  #markup.add(choose7)
  #markup.add(choose8)
      bot.send_message(message.chat.id,"Which Command You want to try?", reply_markup=markup)
    elif(com>username):
      user1=bot.reply_to(message,"GO UP!")
      bot.register_next_step_handler(user1,Game)
    else:
      user1=bot.reply_to(message,"GO DOWN!")
      bot.register_next_step_handler(user1,Game)
    
 
@bot.message_handler(commands=['age'])  #decorator
def get_age(message):
  age=bot.reply_to(message,"Enter the date of birthday: exp:1400/1/1")
  bot.register_next_step_handler(age,Age)
def Age(message):
  year=1400
  month=9
  day=10
  listage=message.text.split("/")
  listage[0]=int(listage[0])
  listage[1]=int(listage[1])
  listage[2]=int(listage[2])
  if(day<listage[2]):
    resD=(day+30)-listage[2]
    month-=1
  else:
    resD=day-listage[2]
  if(month<listage[1]):
    resM=(month+12)-listage[1]
    year-=1
  else:
    resM=month-listage[1]
  resY=year-listage[0]
  bot.reply_to(message, str(resY)+"Years\n"+str(resM)+"Months\n"+str(resD)+"Days")
 
@bot.message_handler(commands=['voice'])  #decorator
def get_text1(message):
  txt=bot.reply_to(message,"TEXT: ")
  bot.register_next_step_handler(txt,Voice)
def Voice(message):
  Text=message.text
  myobj = gTTS(text=Text, lang='en', slow=False)
  myobj.save("VOICE.mp3")
  ttv=open("VOICE.mp3","rb")
  bot.send_voice(message.chat.id, ttv)
 
@bot.message_handler(commands=['max'])  #decorator
def get_array(message):
  arry=bot.reply_to(message,"Enter elements of array")
  bot.register_next_step_handler(arry,Max)
def Max(message):
  numarray=message.text.split(" ")
  for i in range(len(numarray)):
    numarray[i]=int(numarray[i])
  bot.reply_to(message, max(numarray))
 
@bot.message_handler(commands=['argmax'])  #decorator
def get_arrayind(message):
  arry=bot.reply_to(message,"Enter elements of array")
  bot.register_next_step_handler(arry,Argmax)
def Argmax(message):
  numarray=message.text.split(" ")
  for i in range(len(numarray)):
    numarray[i]=int(numarray[i])
  bot.reply_to(message, numarray.index(max(numarray)))


 
@bot.message_handler(commands=['qrcode'])  #decorator
def get_text(message):
  txt=bot.reply_to(message,"TEXT: ")
  bot.register_next_step_handler(txt,QRcode)
def QRcode(message):
  img=qrcode.make(message.text)
  img.save('QRphoto.png')
  data=open('QRphoto.png','rb')
  bot.send_photo(message.chat.id, data)
 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "It's not in commands!!")
 
bot.polling(none_stop=True)
