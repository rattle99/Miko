import discord
from discord.ext import commands
import getcoin


user_token = open("token", "r")
TOKEN = user_token.read().rstrip()
user_token.close()
print('Bot token :', TOKEN)


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready!')
    print('Logged in as {0.user}'.format(client))

@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send('Pong!')

def makeEmbed(name):
    embed = discord.Embed(
        colour = discord.Colour.from_rgb(255, 220, 156)
    )

    coin = getcoin.Coin(name)
    
    embed.set_footer(text = 'Prices from CoinMarketCap', icon_url = 'https://i.imgur.com/N04AybW.jpg')
    embed.set_author(name = name.capitalize())
    embed.add_field(name = 'Price', value = coin.price, inline = True)
    embed.add_field(name = 'Rank', value = coin.rank, inline = True)
    embed.add_field(name = 'Swing', value = coin.swing, inline = False)
    embed.add_field(name = 'Market Cap', value = coin.market_cap, inline = True)
    embed.add_field(name = '24H Volume', value = coin.volume, inline = True)

    return embed

@client.command(aliases=['Burst'])
async def burst(ctx):
    embed = makeEmbed('burst')
    embed.set_author(name = 'BURST', icon_url = 'https://i.imgur.com/ipP9Bu3.png')

    await ctx.send(embed = embed)

@client.command(aliases=['Bhd'])
async def bhd(ctx):
    embed = makeEmbed('bitcoinhd')
    embed.set_author(name = 'BitcoinHD', icon_url = 'https://s2.coinmarketcap.com/static/img/coins/64x64/3966.png')

    await ctx.send(embed = embed)

@client.command(aliases=['Bitcoin','Btc','bitcoin'])
async def btc(ctx):
    embed = makeEmbed('bitcoin')
    embed.set_author(name = 'Bitcoin', icon_url = 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png')

    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(3, 30, commands.BucketType.user)
async def get(ctx, name):
    embed = makeEmbed(name)

    await ctx.send(embed = embed)

@get.error
async def get_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Calm down, I don\'t want to be rate limited, please try again in {:.0f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

client.run(TOKEN)    
