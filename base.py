import discord
import configparser
import replies

from secrets.token_secret import get_token


TOKEN = get_token()
client = discord.Client()

config = configparser.ConfigParser()
config.read('config.ini')

MEMES = config['CHANNELS']['memes']
UPVOTE = config['EMOJIS']['upvote']
DOWNVOTE = config['EMOJIS']['downvote']


@client.event
async def on_message(message):
    # No Self Response. :yeet:.
    if message.author == client.user:
        return
    # Michael Mode
    elif message.content.lower().endswith('.') and message.content.lower()[:-1] in replies.replies:
        await respond(message.channel, replies.replies[message.content.lower()[:-1]] + '.')
    # Reply Responses
    elif message.content.lower() in replies.replies.keys():
        await respond(message.channel, replies.replies[message.content.lower()])
    # No u Triggers
    for trigger in replies.nou_triggers:
        if trigger in message.content.lower():
            if message.content.endswith('.'):
                await respond(message.channel, "No u.")
            else:
                await respond(message.channel, "No u")
            break

    # Upvote/Downvote Automatically.
    if message.channel.id == MEMES and len(message.attachments) > 0:
        await client.add_reaction(message, UPVOTE)
        await client.add_reaction(message, DOWNVOTE)
        # Greg Meme™
        if message.author.id == '148254683704721408':
            await respond(message.channel, "Greg Meme:tm:")


@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="on Michael's MacBook."))

client.run(TOKEN)