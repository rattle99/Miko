import discord
from discord.ext import commands


TOKEN = 'NTkzNDQ3OTQxNzU5NTY1ODQ3.XROH7A.JqYYcSHVxatvOeI883SXQhJi584'


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


client.run(TOKEN)    
