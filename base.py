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
    elif message.content.lower() in replies.keys():
        await respond(message.channel, replies[message.content] if not message.content.endswith('.') else replies[message.content] + '.') 
    #if message.content.startswith('Yeet'):
    #    msg = 'Yeet {0.author.mention}'.format(message)
    #    await respond(message.channel, msg)
    if message.author == 'Greg':
        print('Greg Meme')

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