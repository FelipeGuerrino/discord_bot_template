import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

dev=int(os.getenv('DEV'))
prefix=","

bot = commands.Bot(command_prefix=prefix)

def is_dev():
    """Checks if the author ID is equal to the dev ID
    """
    async def predicate(ctx):
        return ctx.author.id == dev
    return commands.check(predicate)


@bot.event
async def on_ready():
    print('Bot ready!')

@bot.command()
@is_dev()
async def on(ctx):
    await bot.change_presence(status=discord.Status.online)

@bot.command()
@is_dev()
async def idle(ctx):
    await bot.change_presence(status=discord.Status.idle)

@bot.command()
@is_dev()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'Cog {extension} loaded.')

@bot.command()
@is_dev()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'Cog {extension} unloaded.')

@bot.command()
@is_dev()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'Cog {extension} reloaded succesfully.')
#load/reload/unload


for filename in os.listdir('src/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(os.getenv('TOKEN')) #.env
