
from telethon import TelegramClient, events
import config
import get_verses

api_id = config.my_api_id
api_hash = config.my_api_hash
bot_token = config.my_bot_token

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

admin_user_id = config.admin_user_id

# read new messages
@bot.on(events.NewMessage)
async def new_message_handler(event):
    log(event.raw_text)
        
    if ("stop" or "Stop") in event.raw_text:
        print("program killed")
        await event.reply("see you later!")
        quit()
    
    elif( "bible man" in event.raw_text.lower()):
        ref = event.raw_text.split(" ")
        verse_data = get_verses.BibleVerse(ref[2], ref[3], ref[4]).result()
        await event.reply(verse_data)


def log(text):
    with open('log.txt', 'a') as f:
        f.write(text + "\n")
    print("[Receieved Message]: " + text)


# run the bot
if __name__ == '__main__':
    bot.start()
    print("Running  * B I B L E  M A N *...")
    bot.run_until_disconnected()
