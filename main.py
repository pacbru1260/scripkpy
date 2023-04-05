import discord
from discord import app_commands
from discord.ext import commands
import json
import NekoMimi as neko

print(neko.banner("scripkpy"))

raw = neko.ReadFromFile('token.json')
token = json.loads(raw)['token']