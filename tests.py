from discord.ext import commands
from bot import PawBot

class Tests(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    #Seems to work now?
    @commands.command()
    async def generalTest(self, ctx):
        await ctx.send('STANDARD TEST:\nRETURNED TRUE. TEST SUCESSFUL.')
        #channel = 
        #await channel.send('STANDARD TEST:\nRETURNED TRUE. TEST SUCESSFUL.')

async def setup(bot):
    await bot.add_cog(Tests(bot))
