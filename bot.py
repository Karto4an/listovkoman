import os
import discord
import random

client = discord.Client()  #initializing some stuff
random.seed()

#getting token from heroku vars
def index(request):
    print(os.environ.get('BOT_TOKEN'))

ads = ["Кима","Музыкант","Вібачте","АТБ","Жираф","Челиха","Шо ты сказааааав?","Беблеотечка"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send(random.choice(ads), tts = True)

    if message.content.startswith('$hello'):
        await message.channel.send("1xbet", tts = True)
        
client.run(token)
