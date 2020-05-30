import discord
from discord.ext import commands

TOKEN = '7JNP2mdOy6_9irTutM_eaEGAJq9SEvj5'
bot = commands.Bot

@bot.command(pass_context=True, self=0)
async def test(ctx, arg):
	await ctx.send(arg)

bot.run(TOKEN)