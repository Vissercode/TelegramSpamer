from pyrogram import Client, filters
import time



api_id = ''
api_hash = ''
app = Client('account',api_id,api_hash)

message_text = """
**🐍 Python coder 🐍**

Давно ищешь человека, который мог бы реализовать твой проект?
Не успеваешь сделать лабу? 
Срочно нужно спарсить данные с сайта?
Я помогу тебе.
3-ех летний опыт в программировании на Python

__🦾 Чекеры
🦾 Парсеры
🦾 Боты
🦾 Работа с соц. сетями__

"""


chat = {
-1001266598286:'📝 Связь: @vissercode\n🎩 Гарант: @scrooge_garantbot',
-1001332422950:"📝 Связь: @vissercode\n🎩 Гарант: @lolzteam_garant_bot",
-1001376947189:"#ищуработу"}
def main():
    with app:
        for i in chat:
            try:
                with open('banner.png') as ft:
                    app.send_photo(i, ft, caption=f'{message_text}{chat.get(i)}',)
                
            except:
                try:    
                    print(i)
                    print(chat.get(i))
                    app.send_message(i,f'{message_text}{chat.get(i)}') 
                except:
                    continue          

if __name__ == '__main__':
    while True:
        main()
        time.sleep(1800)
