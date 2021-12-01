import telebot
import random
print("Hello Google")
bot = telebot.TeleBot("2125911362:AAGIRV6lphNHrEU2GxRjB5c2Lus8b9SUdAc")


@bot.message_handler(commands=['start'])  #decorator
def welcome(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(message, """کامند start/
با نام کاربر، خوش آمدید چاپ کند. مثلا (sajjad خوش آمدی) 
کامند game/ 
بازی حدس عدد اجرا شود. کاربر یک عدد حدس میزند و بات راهنمایی می‌کند (برو بالا، برو پایین، برنده شدی) - در هنگام بازی، یک دکمه new game در پایین بات مشاهده شود.
کامند age/
تاریخ تولد را به صورت هجری شمسی دریافت نماید و سن را محاسبه نماید. (برای راهنمایی به آدرس اینستاگرامی pylearn@ مراجعه نمایید)
کامند voice/
یک جمله به انگلیسی از کاربر دریافت نماید و آن را به صورت voice ارسال نماید. (برای راهنمایی به آدرس اینستاگرامی pylearn@ مراجعه نمایید)
کامند max/
یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و بزرگترین مقدار را چاپ نماید.
کامند argmax/
یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و اندیس بزرگترین مقدار را چاپ نماید.
کامند qrcode/
یک رشته از کاربر دریافت نماید و qrcode آن را تولید نماید.
""")
 
@bot.message_handler(commands=['game'])  #decorator
def Game(message):
  com=random.randint(0,100)
  user=bot.send_message(message.chat.id, "Enter Number: ")
  bot.register_next_step_handler(user,Game)
  #user = bot.get_me()
  #print(user)
  #user=int(message.text)
  while(True):
    #bot.reply_to(message, "HIIII ")
    #user=int(input())
    if(com==user):
      bot.reply_to(user,"WELL!!!")
    elif(com>user):
      bot.reply_to(user,"GO UP!")
    else:
      bot.reply_to(user,"GO DOWN!")
 
@bot.message_handler(commands=['age'])  #decorator
def Age(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(commands=['voice'])  #decorator
def Voice(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(commands=['max'])  #decorator
def Max(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(commands=['argmax'])  #decorator
def Argmax(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(commands=['qrcode'])  #decorator
def QRcode(message):
  bot.reply_to(message, "Hello, Welcome to this bot....How can i help you?")
 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "MESSAGE")
 
bot.infinity_polling()