from typing import Optional
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

async def send_file(comic_number, message):
    context = xkcd.getContext()
    xkcd.setChannel(context.channel)
    xkcd.setMessageAuthor(context.message.author.name) 
    xkcd.pullComic(comic_number)

    title = xkcd.getComicTitle()
    date = xkcd.getComicDate()
    # path = xkcd.getPath()
    comic_number = xkcd.getComicNumber()

    embed = discord.Embed(
        description=f'`{message} \r Date: {date}`',
        title=f'`Title: {title}`',
        color=0x00ff00,
      
    ) 
    embed.add_field(name='Comic Number:',
                    value=f'`{comic_number}`',
                    inline=False)
    embed.set_image(url=xkcd.getImageURL())

    
    message = await context.channel.send(embed=embed)

    xkcd.setMessageID(message.id)
    
    await add_reactions(message)

async def delete_message():
    channel = xkcd.getChannel()
    message_id = xkcd.getMessageID()
   
    message = await channel.fetch_message(message_id)
    await message.delete()

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
    xkcd.setContext(ctx)

    current_comic_num = xkcd.getLatestComicNumber()
    random_comic_num = rd.randint(1,current_comic_num)

    message ='There you go!'
    await send_file( random_comic_num,message)
   
    

@client.command()
async def first(ctx):
    """Pulls the very first XKCD comic"""
    xkcd.setContext(ctx)

    message = 'XKCD\'s first ever comic!'
    await send_file(1,message)
    
@client.command()
async def latest(ctx):
    "Sends the latest XKCD comic"
    xkcd.setContext(ctx)

    latest_comic_number = xkcd.getLatestComicNumber()
    
    message = 'XKCD\'s latest comic!'
    await send_file(latest_comic_number,message)




@client.event
async def on_reaction_add(reaction,user):
    
    if(client.user.name != user.name) and (reaction.message.id == xkcd.getMessageID()):

        if(reaction.emoji == constants.left_arrow_emoji):
                new_comic_number = xkcd.getLatestComicNumber() if xkcd.getComicNumber() == 1 else xkcd.getComicNumber() - 1
                message = 'Going back to the latest comic' if new_comic_number == 1 else 'Here is the previous comic'
        elif(reaction.emoji == constants.right_arrow_emoji):
                new_comic_number = 1 if xkcd.getComicNumber() == xkcd.getLatestComicNumber() else xkcd.getComicNumber() + 1
                message = 'The previous comic was the latest one. Here is the first-ever comic' if new_comic_number == 1 else 'Anotha One!'
        elif(reaction.emoji == constants.random_emoji):
            new_comic_number = rd.randint(1,xkcd.getLatestComicNumber())
            message = 'A random one!'
        await delete_message()
        await send_file(new_comic_number,message)
        
def main():    
    client.run(BOTTOKEN)
    

if __name__  == '__main__':
    xkcd = XKCD()
    constants = Constants()
    main()