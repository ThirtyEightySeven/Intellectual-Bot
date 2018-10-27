import discord
import json
import configparser

from secrets.token_secret import get_token


TOKEN = get_token()
client = discord.Client()
data = open('replies.json')
replies = json.load(data)

config = configparser.ConfigParser()
config.read('config.ini')

MEMES = config['CHANNELS']['memes']
UPVOTE = config['EMOJIS']['upvote']
DOWNVOTE = config['EMOJIS']['downvote']

@client.event
async def on_message(message):
    print(type(message.channel))

    if message.author == client.user:
        return
    elif message.content.lower().endswith('.'):
        await respond(message.channel, replies[message.content.lower()[:-1]] + '.')
    elif message.content.lower() in replies.keys():
        await respond(message.channel, replies[message.content.lower()])
    elif message.channel.id == '505553720294113281':
        await react('hello', None)
    elif message.channel.id == '505550463408799774':
        await respond(message.channel, 'Greg Meme™')
        if message.author.id == '148254683704721408':
            print('DEBUG: GREG')          
            #  await respond(message.channel, str(message.channel))



@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == MEMES:
        await client.add_reaction(message, UPVOTE)
        await client.add_reaction(message, DOWNVOTE)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
