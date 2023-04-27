from discord.ext import commands
from bot import PawBot

class Tests(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @commands.command()
    async def generalTest(self, ctx):
        await ctx.send(':3')

    @commands.command()
    async def kill(self, ctx):
        await ctx.send("*dies*")

async def setup(bot):
    await bot.add_cog(Tests(bot))
