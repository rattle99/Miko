import discord
from discord.ext import commands


TOKEN = 'NTkzNDUyODI2Mzc4ODk1Mzgz.XROljQ.xCHjkkqQKzRrkj3Z9_qya2qWq_8'


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def burst(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = 'Prices from CoinMarketCap', icon_url = 'https://i.imgur.com/N04AybW.jpg')
    embed.set_author(name = 'BURST', icon_url = 'https://i.imgur.com/ipP9Bu3.png')
    embed.add_field(name = 'Price', value = 'Field Value', inline = False)
    embed.add_field(name = 'Swing', value = 'Field Value', inline = False)
    embed.add_field(name = 'Rank', value = 'Field Value', inline = True)
    embed.add_field(name = 'Market Cap', value = 'Total Cap', inline = True)
    embed.add_field(name = '24H Volume', value = 'Volume', inline = True)

    await ctx.send(embed = embed)

client.run(TOKEN)    
