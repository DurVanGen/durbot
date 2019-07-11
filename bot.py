import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = ("NTk4OTIxMDU4OTIxNDgwMTkz.XSdtWg.XT7dfR6vNBdpWYwvSXEQLYfqJDQ")
Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='with Generator'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel,'<@%s> visit #how-to-gen channel'  %(message.author.id))
    if message.content.startswith('!fortnite'):
        randomlist = ["Your link to Fortnite accounts: https://filemedia.net/27527/fortnite","Your link to Fortnite accounts: https://up-to-down.net/27832/1","Your link to Fortnite accounts: https://up-to-down.net/27527/fortnite02"]
        await client.send_message(message.author,(random.choice(randomlist)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!minecraft'):
        randomlist1 = ["Your link to Minecraft accounts: https://link-to.net/27527/Minecraft001","Your link to Minecraft accounts: https://up-to-down.net/27527/minecrafts","Your link to Minecraft accounts: https://filemedia.net/27527/Minecraft"]
        await client.send_message(message.author,(random.choice(randomlist1)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!nitro'):
        randomlist2 = ["We are really sorry but we are currently out of nitro links"]
        await client.send_message(message.author,(random.choice(randomlist2)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content == '!spotify':
        randomlist3 = ["Your link to Spotify accounts: https://direct-link.net/27527/spotify4","Your link to Spotify accounts: https://direct-link.net/27527/spotify2"]
        await client.send_message(message.author,(random.choice(randomlist3)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!nord'):
        randomlist4 = ["Your link to NordVPN accounts: https://filemedia.net/27527/NordVPN"]
        await client.send_message(message.author,(random.choice(randomlist4)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!origin'):
        randomlist5 = ["Your link to Origin accounts: https://link-to.net/27527/origin","Your link to Origin accounts: https://up-to-down.net/27527/origin2","Your link to Origin accounts: https://direct-link.net/27527/origin3"]
        await client.send_message(message.author,(random.choice(randomlist5)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!hulu'):
        randomlist6 = ["Your link to Hulu accounts: https://filemedia.net/27527/hulu","Your link to Hulu accounts: https://filemedia.net/27527/hulu2"]
        await client.send_message(message.author,(random.choice(randomlist6)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!steam'):
        randomlist7 = ["Your link to Steam accounts: https://filemedia.net/27527/steam"]
        await client.send_message(message.author,(random.choice(randomlist7)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!pinterest'):
        randomlist8 = ["Your link to Pinterest accounts: https://link-to.net/27527/pinterest"]
        await client.send_message(message.author,(random.choice(randomlist8)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!udemy'):
        randomlist9 = ["Your link to Udemy accounts: https://up-to-down.net/27527/udemy","Your link to Udemy accounts: https://filemedia.net/27527/udemy2"]
        await client.send_message(message.author,(random.choice(randomlist9)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!uplay'):
        randomlist10 = ["Your link to Uplay accounts: https://up-to-down.net/27527/uplay2","Your link to Uplay accounts: https://up-to-down.net/27527/uplay"]
        await client.send_message(message.author,(random.choice(randomlist10)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!crunchyroll'):
        randomlist11 = ["Your link to Crunchyroll accounts: https://up-to-down.net/27527/crunchyroll"]
        await client.send_message(message.author,(random.choice(randomlist11)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!scribd'):
        randomlist12 = ["Your link to Scribd accounts: https://direct-link.net/27527/Scribd"]
        await client.send_message(message.author,(random.choice(randomlist12)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!grammarly'):
        randomlist13 = ["Your link to Grammarly accounts: https://direct-link.net/27527/grammarly"]
        await client.send_message(message.author,(random.choice(randomlist13)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!fuckbook'):
        randomlist14 = ["Your link to Fuckbook accounts: https://filemedia.net/27527/fcbbook"]
        await client.send_message(message.author,(random.choice(randomlist14)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!familyowner'):
        randomlist15 = ["Your link to Familyowner accounts: https://direct-link.net/27527/familyowner"]
        await client.send_message(message.author,(random.choice(randomlist15)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content == '!familyowner':
        randomlist16 = ["Your link to download Spotify Generator is ready: https://direct-link.net/27527/SpotifyGenerator001"]
        await client.send_message(message.author,(random.choice(randomlist16)))
        await client.send_message(message.channel,"Check your DM's")



client.run(TOKEN)
