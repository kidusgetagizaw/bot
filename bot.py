import telebot
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="bk7pnsmdq1aanltzjnlj-mysql.services.clever-cloud.com",
  user="uwjaio6g2ghrakr1",
  password="mu5qlNLAB2ssrWMp0KZ0",
  database="bk7pnsmdq1aanltzjnlj"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM TELEGRAM")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
mycursor.close()
mydb.close()
TOKEN='6380507542:AAFX88kcmwP5qsx1gfDBDdcu8PIZejk0UVw'
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','START'])
def start(message):
  bot.send_message(message.from_user.id,'hello user this is created by kidus geta')
test=True
@bot.message_handler(func = lambda message: True)
def Telegram_bots(message):
    global mydb,test
    mycursor = mydb.cursor()
  
    mycursor.execute("INSERT INTO TELEGRAM (id2,name,message,seen) VALUES ('"+str(message.from_user.id)+"','"+message.from_user.first_name+"','"+message.text+"','false')")
    mydb.commit()
    mycursor.close()
    mydb.close()
    if test:
      while True:
        test=False
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM TELEGRAM")
        myresult = mycursor2.fetchall()
        for x in myresult:
          if x[4] == 'sender':
            bot.send_message(x[1],x[3])
            
            mycursor3 = mydb.cursor()
            mycursor3.execute("UPDATE TELEGRAM SET seen = 'sended' WHERE seen = 'sender'")
            mydb.commit()
            mycursor3.close()
            mydb.close()
        time.sleep(1)
bot.infinity_polling()
