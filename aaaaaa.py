import discord
from discord.ext import commands
from itertools import cycle
import asyncio
from discord.ext import tasks

client=commands.Bot(command_prefix='!')
status=cycle(['명령어를','졸려하며'])

@client.event
async def on_ready():
    print('ready')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

client.run('token')
