import os
import logging

import requests
import discord
from dotenv import load_dotenv
import shutil

# Join link
# https://discord.com/api/oauth2/authorize?client_id=943603635319885884&permissions=8&scope=bot

load_dotenv()
logging.basicConfig(level=logging.INFO, filename="log.log")
bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is up")

@bot.event
async def on_guild_join(guild: discord.Guild):
    for member in guild.members:
        print(f"Downloading {member.display_name}")
        try:
            avatar = member.avatar
            if type(avatar) != None:
                filename = member.name
                r = requests.get(avatar.url, stream=True)
                if r.status_code == 200:
                    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                    r.raw.decode_content = True
                    
                    # Open a local file with wb ( write binary ) permission.
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        
                    print('Image sucessfully Downloaded: ',filename)
                else:
                    print('Image Couldn\'t be retreived')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    bot.run(token=os.environ.get('botToken'))