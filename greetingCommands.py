import discord
#from discord.ext.commands.cog import Cog
from discord.ext import commands

# from bot import PawBot

# client = PawBot()
# def setup(client):
#     client.add_cog(Cog(client))

class Greetings(commands.Cog):
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member
