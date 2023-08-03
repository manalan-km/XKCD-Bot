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





async def add_reactions(msg):
    await msg.add_reaction(f'{constants.left_arrow_emoji}')
    await msg.add_reaction(f'{constants.right_arrow_emoji}')
    await msg.add_reaction(f'{constants.random_emoji}')

async def send_file(context):
    xkcd.setMessageAuthor(context.message.author.name) 

    title = xkcd.getComicTitle()
    date = xkcd.getComicDate()
    path = xkcd.getPath()
    comic_number = xkcd.getComicNumber()

    await context.send(f'Title: `{title}`')
    await context.send(f'Published Date: `{date}`')
    await context.send(f'Comic Number: `{comic_number}`')
    
    message = await context.send(file = discord.File(path))
    xkcd.setMessageID(message.id)
    await add_reactions(message)

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
    
    current_comic_num = xkcd.getLatestComicNumber()
    random_comic_num = rd.randint(1,current_comic_num)
    xkcd.pullComic(random_comic_num)
    await ctx.send('There you go!')
    await send_file(ctx)
   
    

@client.command()
async def first(ctx):
    xkcd.pullComic()
    await ctx.send('XKCD\'s first ever comic!')
    await send_file(ctx)
    

@client.command()
async def latest(ctx):
    latest_comic_number = xkcd.getLatestComicNumber()
    xkcd.pullComic(latest_comic_number)
    await ctx.send('XKCD\'s latest comic!')
    await send_file(ctx)
        

@client.event
async def on_reaction_add(reaction,user):
    
    if(client.user.name != user.name) and (reaction.message.id == xkcd.getMessageID()):
        print(f'{user.name} reacted {reaction.emoji}')
        
            
    
def main():    
    client.run(BOTTOKEN)
    

if __name__  == '__main__':
    xkcd = XKCD()
    constants = Constants()
    main()