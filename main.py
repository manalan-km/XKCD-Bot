import discord
from discord.ext import commands

from apitokens import *

import requests
import random as rd
import os

from additional_functions import *

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


@client.command()
async def random(ctx):
    "Pulls a random XKCD comic by using >random."
    
    current_comic_num = getLatestComicNumber()

    random_comic_num = rd.randint(1,current_comic_num)

    title = pullComic(random_comic_num)

    await ctx.send('There you go!')
    await ctx.send(f'Title: `{title}`')
    message = await ctx.send(file = discord.File(path))
    # await.ctx.add_reaction('')

@client.command()
async def first(ctx):
    first_comic, title = pullComic()
        
client.run(BOTTOKEN)