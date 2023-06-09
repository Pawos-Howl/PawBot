import discord
from discord.ext import commands
from bot import PawBot

class botDisable(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client
        self._last_member = None

    @commands.command()
    async def killBot(self, ctx):
        if int(ctx.author.id) == 979210001556070491:
            # This will cause many errors on the discord package, but it works. "https://www.scaler.com/topics/how-to-end-program-in-python/" if I want to fix it
            await ctx.send("Terminating...")
            exit("Terminating")
        else:
            await ctx.send('>:c\nYou are not allowed to do that!')

async def setup(bot):
    await bot.add_cog(botDisable(bot))
