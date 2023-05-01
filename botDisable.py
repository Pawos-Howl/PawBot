import discord
from discord.ext import commands
from bot import PawBot

class botDisable(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client
        self._last_member = None

    @commands.command()
    async def killBot(self, ctx):
        if discord.Object(id=int(ctx.author.id)) == self.client.MY_USER_ID:
            await ctx.send("PawBot will now try to stop itself.")
            try:
                quit()
            except:
                await ctx.send("There has been an error. Pawbot gets to live. >:3")
        else:
            await ctx.send('>:c\nYou are not allowed to do that!')

async def setup(bot):
    await bot.add_cog(botDisable(bot))
