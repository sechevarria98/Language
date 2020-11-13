import discord
import random
from discord.ext import commands

class Responses(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['test'])
    async def magicConch(self, ctx, *, question):
        response = [ 
            'It is certain',
            'Without a doubt',
            'You may rely on it',
            'Yes definitely',
            'It is decidedly so',
            'As I see it, yes',
            'Most likely',
            'Yes',
            'Outlook good',
            'Signs point to yes',
            'Reply hazy try again',
            'Better not tell you now',
            'Ask again later',
            'Cannot predict now',
            'Concentrate and ask again',
            'Don’t count on it',
            'Outlook not so good',
            'My sources say no',
            'Very doubtful',
            'My reply is no']
        await ctx.send(f'{random.choice(response)}')

def setup(client):
    client.add_cog(Responses(client))