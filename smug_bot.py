from telethon import TelegramClient, events
import re
import config

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
        
    if ("kill" or "Kill") in event.raw_text:
        print("program killed")
        await event.reply("smug has left")
        quit()
    
    elif(len(event.raw_text) < 220):
        smug_response = event.raw_text + "\U0001F60F"
        await event.reply(smug_response)


# run the bot
if __name__ == '__main__':
    bot.start()
    print("Running...")
    bot.run_until_disconnected()
