import discord
import json
from secrets.token_secret import get_token


TOKEN = get_token()
client = discord.Client()
data = open('replies.json')
replies = json.load(data)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.lower().endswith('.'):
        await respond(message.channel, replies[message.content.lower()[:-1]] + '.')
    elif message.content.lower() in replies.keys():
        await respond(message.channel, replies[message.content.lower()])
    elif message.author.id == '148254683704721408' and message.channels == '505550463408799774':
        await respond(message.channel, 'Greg Meme™')


@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
