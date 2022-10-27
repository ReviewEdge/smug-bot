from telethon import TelegramClient, events
import re
import config
import bee_movie
import bible

api_id = config.my_api_id
api_hash = config.my_api_hash
bot_token = config.my_bot_token

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

admin_user_id = config.admin_user_id


# bot_is_on = True


# read new messages
@bot.on(events.NewMessage)
async def new_message_handler(event):
    # if bot_is_on:

    # user_id = str(event.peer_id.user_id)

    # if "stop" in event.raw_text:
    #     bot_is_on = False

    log(event.raw_text)
        
    if ("stop" or "Stop") in event.raw_text:
        print("program killed")
        await event.reply("see you later\U0001F60F")
        quit()
    
    elif( "the bible" in event.raw_text.lower()):
        smug_response = bible.bible
        await event.reply(smug_response)

    elif( "bee movie" in event.raw_text.lower()):
        smug_response = bee_movie.script
        await event.reply(smug_response)

    elif(( "\U0001F617" in event.raw_text) and (len(event.raw_text) < 220)):
        smug_response = ""
        for c in event.raw_text:
            smug_response = smug_response + c + " "

        await event.reply(smug_response)

    elif(( "\U0001F619" in event.raw_text) and (len(event.raw_text) < 89)):
        smug_response = ""
        counter = 0
        for c in event.raw_text:
            smug_response = smug_response + c + " "*counter
            counter+=1

        await event.reply(smug_response)

    elif(len(event.raw_text) < 220):
        smug_response = event.raw_text + "\U0001F60F"
        await event.reply(smug_response)


def log(text):
    with open('log.txt', 'a') as f:
        f.write(text + "\n")
    print("[Receieved Message]: " + text)


# run the bot
if __name__ == '__main__':
    bot.start()
    print("Running...")
    bot.run_until_disconnected()
