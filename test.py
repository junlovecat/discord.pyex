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

@client.command()
async def ping(ctx):
    print('pong')

@client.command()
async def hi(ctx,name):
    print('hi, '+name)

@client.command()
async def hello(ctx,*,name):
    print('hello, '+name)

@client.command(aliases=['aa','aaa'])
async def a(ctx):
    print('aaaaa')

@client.command()
async def show_embed(ctx):
    embed=discord.Embed(title='embed',description='embed',color=discord.Color.blue())
    embed.add_field(name='name1',value='value1',inline=True)
    embed.add_field(name='name2',value='value2',inline=False)

@client.command()
async def echo(ctx):
    try:
        msg=await client.wait_for("message",timeout=30)
        await ctx.send(str(msg.author)+':'+str(msg.content))
    except asyncio.TimeoutError:
        await ctx.send('time up')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

client.run('token')