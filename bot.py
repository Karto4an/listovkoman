import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

client = discord.Client(command_prefix = ".")

load_dotenv()
token = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
	print("ready")
	
@client.command
async def ban(ctx, member: discord.Member, *, reason = None):
	await member.ban(reason=reason)
client.run(token)
