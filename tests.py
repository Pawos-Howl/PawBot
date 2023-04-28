import discord
from discord.ext import commands
from bot import PawBot

class Tests(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client
        self._last_member = None

    @commands.command()
    async def generalTest(self, ctx):
        await ctx.send(':3')

    @commands.command()
    async def cutie(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'>w<\nn-nuu. das you, {member.name}~')
        else:
            await ctx.send(f'>//w//< f-fine. I admit it {member.name}, I am a cutie. ~~only to you though~~')
        self._last_member = member

async def setup(bot):
    await bot.add_cog(Tests(bot))
