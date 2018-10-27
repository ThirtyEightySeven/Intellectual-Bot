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
    if message.author == client.user:
        return
    elif message.content.lower().endswith('.'):
        await respond(message.channel, replies[message.content.lower()[:-1]] + '.')
    elif message.content.lower() in replies.keys():
        await respond(message.channel, replies[message.content.lower()])


@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == MEMES and len(message.attachments) > 0:
        await client.add_reaction(message, UPVOTE)
        await client.add_reaction(message, DOWNVOTE)
    if message.channel.id == MEMES and message.author.id == '148254683704721408':
        await respond(message.channel, "Greg Meme:tm:")        


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
