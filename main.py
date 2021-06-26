import json
import discord

with open('\My Drive\Work\Python_project\Discord_Weather_Bot\secrets.json', 'r') as secrets_file:
    secrets = json.load(secrets_file)

token = secrets['token']
api_key = secrets['api_key']
client = discord.Client()

client.run(token)
