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
        await message.channel.send('Hello!')
        
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
BOT1 = str("NzE2MzAxNjYzMTQwMzE1MTQ3")
BOT2 = str(".XtKXyQ.KXhvyWv3b_5sbBWzBYap3Uh9Kgw")

client.run(BOT1+BOT2)
