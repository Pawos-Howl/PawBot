from discord.ext import commands
from bot import PawBot

class Tests(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @commands.command()
    async def generalTest(self, ctx):
        await ctx.send(':3')
        
async def setup(bot):
    await bot.add_cog(Tests(bot))
