# Daniel Holmes
# 2018/11/2
# bot_ross.py


import discord
import os
from bot_commands import sobel_command, compression_command


token = os.environ['token']
client = discord.Client()


@client.event
async def on_ready():
    """ Update bot status message """
    await client.change_presence(game=discord.Game(name='Happy Little Trees'))


@client.event
async def on_message(message):
    """ Receive messages """
    if message.content.upper().startswith('!SOBEL'):
        await sobel_command(client, message)

    elif message.content.upper().startswith('!COMPRESSION'):
        await compression_command(client, message)

    elif message.content.upper().startswith('!HELP'):
        await client.send_message(message.channel, "Commands: \n!help \n!sobel [url] \n!compression [number 2-16] [url]")

client.run(token)
