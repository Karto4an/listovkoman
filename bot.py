import os

import discord
import random

from dotenv import load_dotenv

count = 0

client = discord.Client()  #initializing some stuff
random.seed()

#getting token from heroku vars
load_dotenv()
token = os.getenv('BOT_TOKEN')

ads = (["Меня создал натурал @Karto4an#0420","88005553535 лучше позвонить чем у кого-то занимать",
        "Каждому сосну за покупку участка в экологически чистой зоне","Мясные продукты отменного качества! За слова отвечаем.",
        "Жираф","Челиха","Шо ты сказааааав?","Беблеотечка"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    count = int("count+1")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=count))
    await message.channel.send(random.choice(ads), tts = True)

    if message.content.startswith('$hello'):
        await message.channel.send("1xbet", tts = True)
        
client.run(token)
