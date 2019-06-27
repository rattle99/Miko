import discord
from discord.ext import commands
import getcoin


user_token = open("token", "r")
TOKEN = user_token.read().rstrip()
user_token.close()
print(TOKEN)


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

    coin = getcoin.Coin()
    
    embed.set_footer(text = 'Prices from CoinMarketCap', icon_url = 'https://i.imgur.com/N04AybW.jpg')
    embed.set_author(name = 'BURST', icon_url = 'https://i.imgur.com/ipP9Bu3.png')
    embed.add_field(name = 'Price', value = coin.price, inline = True)
    embed.add_field(name = 'Rank', value = coin.rank, inline = True)
    embed.add_field(name = 'Swing', value = coin.swing, inline = False)
    embed.add_field(name = 'Market Cap', value = coin.market_cap, inline = True)
    embed.add_field(name = '24H Volume', value = coin.volume, inline = True)

    await ctx.send(embed = embed)

client.run(TOKEN)    
