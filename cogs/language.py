import discord
import random
from discord.ext import commands

#Place Response IF needed
response = [
    
]

#Simply Place Words In here
blacklisted = [
    
]

class Language(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in blacklisted:
            if i in message.content.lower():
                await message.channel.purge(limit=1)
                await message.channel.send(f'{message.author.name} you are a naughty boy')
        if (message.author.id == 123): #Not an actual ID 
            await message.channel.send(f'{random.choice(response)}')


def setup(client):
    client.add_cog(Language(client))