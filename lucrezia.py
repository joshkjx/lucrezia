import discord
import os
from dotenv import load_dotenv
import random
import logging
from discord.ext import commands

load_dotenv()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename= "discord.log", encoding= "utf-8", mode = "w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='?', description= None, intents=intents)

@bot.event
async def on_ready():
    print("Logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)
    

@bot.command()
async def shutdown(ctx):
    await ctx.bot.close()

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(os.getenv('TOKEN'))