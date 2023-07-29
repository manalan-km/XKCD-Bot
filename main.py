import discord
from discord.ext import commands

from apitokens import *

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='>', intents= intents)


@client.event
async def on_ready():

    """Prints when bot is ready to console"""

    
    print(f'{client.user} is ready')
    print('----------------------')

@client.command()
async def hello(ctx):

    """Sends hello when user uses !hello"""
    await ctx.send('Hello there!')


client.run(BOTTOKEN)