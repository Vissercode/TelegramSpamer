from pyrogram import Client, filters
import time
import config
import chats

app = Client('account',config.api_id,config.api_hash)

def main():
    with app:
        for i in chats.chats:
            try:
                with open('banner.jpeg') as ft:
                    app.send_photo(i, ft, caption=f'{config.message_text}{chats.get(i)}',)
                
            except:
                try:    
                    print(i)
                    print(chats.get(i))
                    app.send_message(i,f'{config.message_text}{chats.get(i)}') 
                except:
                    continue          

if __name__ == '__main__':
    while True:
        main()
        time.sleep(config.sleeptime)
