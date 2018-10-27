import discord
import json
from secrets.token_secret import get_token


TOKEN = get_token()
client = discord.Client()
data = open('replies.json')
replies = json.load(data)


@client.event
async def on_message(message):
    print(message.content.endswith('.'))
    if message.author == client.user:
        return
    elif message.content.lower().endswith('.'):
        await respond(message.channel, 'Period boi')
    elif message.content.lower() in replies.keys():
        await respond(message.channel, replies[message.content.lower()])
    elif message.author.id == '148254683704721408':
        await respond(message.channel, 'Greg Meme™')
    #if message.content.startswith('Yeet'):
    #    msg = 'Yeet {0.author.mention}'.format(message)
    #    await respond(message.channel, msg)
    #elif message.author.id == '148254683704721408':
    #    await respond(message.channel, 'Greg Meme™')


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
