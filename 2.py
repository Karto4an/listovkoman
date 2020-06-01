import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("1xbet", tts = True)
     
BOT1 = str("NzE2MzAxNjYzMTQwMzE1MTQ3")
BOT2 = str(".XtKXyQ.KXhvyWv3b_5sbBWzBYap3Uh9Kgw")

client.run(BOT1+BOT2)
