from tkinter import EXCEPTION
import discord
from discord import app_commands
from discord.ext import commands
import json
import NekoMimi as neko

print(neko.banner("scripkpy"))

raw = neko.read('token.json')
token = json.loads(raw)['token']

bot = commands.Bot(command_prefix="&",intents = discord.Intents.all())

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except EXCEPTION as e:
        print(e)

@bot.tree.command(name='hi')
async def _neko(ctx):
    await ctx.response.send_message('hello')

bot.run(token)
