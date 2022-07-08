import discord
import os
from dotenv import load_dotenv
from discord import default_permissions
import random
import logging

load_dotenv()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename= "discord.log", encoding= "utf-8", mode = "w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = discord.Bot(test_guild=[368827007628476416])

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command(name = "hello", description = "Say hello to Lucrezia")
async def hello(ctx):
    await ctx.respond("Good Evening, Dear Guests.")

@bot.command(description = "Roll the Dice, in format Xd Xd Modifier")
async def roll(
    ctx, 
    first: discord.Option(str),
    second: discord.Option(str),
    mod: discord.Option(int) = 0):

    try:   
        d1 = int(first.replace("d", ""))
        d2 = int(second.replace("d",""))
        r1 = random.choice(range(1, d1 + 1))
        r2 = random.choice(range(1, d2 + 1))
        if r1 == r2 >= 6:
            await ctx.respond(":heart_on_fire: **Critical!** :heart_on_fire: ")
        await ctx.respond(f"Result: ({r1}, {r2}) + {mod} = **{r1 + r2 + mod}**")
    
    except (IndexError, ValueError):
        await ctx.respond("Sorry, I don't know what that means.")


@bot.command(description = "Remove the Remnants of the Past. (Clears 14 days of messages)")
@default_permissions(administrator=True)
async def clear(ctx):
    msglist = []
    async for x in ctx.channel.history():
        msglist.append(x)
    await ctx.channel.delete_messages(msglist)

bot.run(os.getenv('TOKEN'))