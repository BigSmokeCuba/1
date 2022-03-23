from client import ObigramClient

def onmessage(update,bot:ObigramClient):
message = bot.sendMessage(update.message.chat.id,'Procesando...')

if __name__ == '__main__':
    bot = ObigramClient('5164781245:AAGtOuaRZs2Ug0MPYUrGgNU7PB1zqFbFkuY')
    bot.onMessage(onmessage)
    bot.run()