import discord
from discord.ext import commands

from apitokens import *

import requests
import random as rd
import os

from xkcd import *
from constants import *

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

async def add_reactions(msg):
    await msg.add_reaction(f'{constants.left_arrow_emoji}')
    await msg.add_reaction(f'{constants.right_arrow_emoji}')
    await msg.add_reaction(f'{constants.random_emoji}')


@client.command()
async def random(ctx):
    "Pulls a random XKCD comic by using >random."
    
    current_comic_num = xkcd.getLatestComicNumber()

    xkcd.message_author = ctx.message.author.name

    random_comic_num = rd.randint(1,current_comic_num)

    xkcd.pullComic(random_comic_num)
    title = xkcd.getComicTitle()
    date = xkcd.getComicDate()
    
    path = xkcd.getPath()

    await ctx.send('There you go!')
    await ctx.send(f'Title: `{title}`')
    await ctx.send(f'Published Date: `{date}`')
    await ctx.send(f'Comic Number: `{random_comic_num}`')
    
    message = await ctx.send(file = discord.File(path))
    xkcd.setMessageID(message.id)
    await add_reactions(message)
    

@client.command()
async def first(ctx):
    xkcd.pullComic()
    title = xkcd.getComicTitle()
    date = xkcd.getComicDate()
    path = xkcd.getPath()
    await ctx.send('XKCD\'s first ever comic!')
    await ctx.send(f'Title: `{title}`')
    await ctx.send(f'Published Date: `{date}`')
    await ctx.send(f'Comic Number: `1`')
    

    message = await ctx.send(file = discord.File(path))
    await add_reactions(message)

@client.command()
async def latest(ctx):
    latest_comic_number = xkcd.getLatestComicNumber()
    xkcd.pullComic(latest_comic_number)
    title = xkcd.getComicTitle()
    date = xkcd.getComicDate()
    path = xkcd.getPath()
    await ctx.send('XKCD\'s latest comic!')
    await ctx.send(f'Title: `{title}`')
    await ctx.send(f'Published Date: `{date}`')
    await ctx.send(f'Comic Number: `{latest_comic_number}`')
    message = await ctx.send(file = discord.File(path))
    await add_reactions(message)
        

@client.event
async def on_reaction_add(reaction,user):
    # print(xkcd.getMessageAuthor() != client.user.name)
    # print(reaction.message.id == xkcd.getMessageID())
    if(client.user.name != user.name) and (reaction.message.id == xkcd.getMessageID()):
        print(f'{user.name} reacted with {reaction.emoji}')
    
def main():    
    client.run(BOTTOKEN)
    

if __name__  == '__main__':
    xkcd = XKCD()
    constants = Constants()
    main()