import discord

color = 0x2F7FCC
keyFeatures = {
    'temp': 'Temperature in Celsius',
    'feels_like': 'Feels like',
    'temp_min': 'Minimum Temperature',
    'temp_max': 'Maximum Temperature'
}


def parseData(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data


def weatherMessage(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather data for {location}.',
        color=color
    )
    for key in data:
        message.add_field(
            name=keyFeatures[key],
            value=str(data[key]),
            inline=False
        )
    return message


def errorMessage(location):
    location = location.title()
    return discord.Embed(
        title='Error!',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
