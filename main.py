import json
from os import name
import discord
from discord.client import Client

with open('Python_project/Discord_Weather_Bot/secrets.json', 'r') as secrets_file:
    secrets = json.load(secrets_file)

token = secrets['token']
api_key = secrets['api_key']
command_prefix = 'w.'
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = f'{command_prefix}[location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        # Sends back the message
        await message.channel.send(message.content)

client.run(token)