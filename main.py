from weather import *
import json
import discord
import requests

with open('secrets.json', 'r') as secrets_file:
    secrets = json.load(secrets_file)


TOKEN = secrets['token']
API_KEY = secrets['api_key']
commandPrefix = 'w.'
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{commandPrefix}[location]'))


@client.event
# If the message is not sent by the bot and it starts with "w.", then send back the weather info.
async def on_message(message):
    if message.author != client.user and message.content.startswith(commandPrefix):
        location = message.content.replace(commandPrefix, '').lower()
        # Proper input of location
        if len(location) >= 1:
            # Get weather data
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
            try:
                data = json.loads(requests.get(url).content)
                data = parseData(data)
                await message.channel.send(embed=weatherMessage(data, location))
            except KeyError:
                await message.channel.send(embed=errorMessage(location))

client.run(TOKEN)
