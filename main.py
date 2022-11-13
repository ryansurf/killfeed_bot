import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from check_log import *
from player_count import *
import time
import random

load_dotenv()
# gets bot and guild(server) token 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = int(os.getenv('CHANNEL'))
PING_CHANNEL=int(os.getenv('PING_CHANNEL'))
# gets parameters for kill_string function
NITRADO_TOKEN = os.getenv('NITRADO_TOKEN')
URL = os.getenv('URL')
# txt file to write to
TXT_FILE = os.getenv('TXT_FILE')
KILL_WAIT = os.getenv('KILL_WAIT')
TIME_WAIT = os.getenv('TIME_WAIT')

# keep track of last kill 

# establishes bot's connection to the server
# command prefix is how we call the bot in discord
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#on ready is a function that is called once bot has connected to the discord
@bot.event
async def on_ready():
    # starts the function that checks the kill logs 
    check_log.start()
    print(f'{bot.user.name} has connected to Discord!')

# bot responds to "!ping" command 
@bot.command(pass_context=True)
async def players(ctx):
    channel = bot.get_channel(PING_CHANNEL)
    players = player_count(NITRADO_TOKEN, URL)
    # strip time stamps stamps away from strings 
    await channel.send("```" + players + "```")


# how to loop(background task)?
@tasks.loop(minutes=1)
async def check_log():
    channel = bot.get_channel(CHANNEL)
    kill = kill_string(NITRADO_TOKEN, URL, TXT_FILE)
    # sends message if a kill has happened
    if kill != '':
        add_twenty(kill, KILL_WAIT)
    # checks for kills that happened 20+ min ago 
    check = check_twenty(KILL_WAIT, TIME_WAIT)
    # sends kills in check to chat
    if len(check) > 0:
            for kills in check:
                kills = kills.split('|', 1)[1].split('|')[0]
                await channel.send("```" + kills + "```")
    # deletes kills that have been sent 
    delete_lines(KILL_WAIT, check)

bot.run(TOKEN)