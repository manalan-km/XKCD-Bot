import discord
from discord.ext import commands

from apitokens import *

import requests
import random
import os


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
    

    current_comic_url = "https://xkcd.com/info.0.json"

    response = requests.get(current_comic_url).json()
    current_comic_num = response['num']
    # print(type(current_comic_num))
    random_comic_number = random.randint(1,current_comic_num)
    #print(f'comic num:{random_comic_number}')
    random_xkcd_url = 'https://xkcd.com/' + str(random_comic_number) + '/info.0.json'
    random_comic_response = requests.get(random_xkcd_url).json()
    random_comic_url = random_comic_response['img']
    random_comic_title = random_comic_response['safe_title']
    random_comic_png = requests.get(random_comic_url)
    if not os.path.exists("./XKCD"):
        os.makedirs("./XKCD")
    path = "./XKCD/XKCD.jpg"
        
    with open(path,'wb') as image:
        image.write(random_comic_png.content)
    await ctx.send('There you go!')
    await ctx.send(f'Title: `**{random_comic_title}**`')
    await ctx.send(file = discord.File(path))



client.run(BOTTOKEN)