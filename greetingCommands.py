import discord
from discord.ext import commands
from bot import PawBot

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

async def setup(bot):
    await bot.add_cog(Greetings(bot))
