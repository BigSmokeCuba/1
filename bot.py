from client import ObigramClient

def onmessage(update,bot:ObigramClient):
message = bot.sendMessage(update.message.chat.id,'Procesando...')

if __name__ == '__main__':
    bot = ObigramClient('5100775831:AAEBSnG12VvRAhvGt875zvpA0LyavpIyzyQ')
    bot.onMessage(onmessage)
    bot.run()
