import discord
from discord.ext import commands, tasks
from itertools import cycle

# pylint: disable=E1101
#Status
status = cycle([
        'Oh boy! 3 A.M!'
        ])

class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('Bot is good to go!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Thats not it bub.')

    @tasks.loop(seconds=3600)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))

def setup(client):
    client.add_cog(Ready(client))