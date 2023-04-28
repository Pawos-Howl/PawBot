import discord
from discord import app_commands
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

    @app_commands.command()
    async def bonk(self, interaction: discord.Interaction, member: discord.Member):
        if member.id == 1093034030745780286: #bot ID, should be fixed to find its own id
            msg = f'Wha- I\'m not bonking myself!\n*bonks {interaction.user.mention}*'
        else:
            msg = f'*bonks {member.mention} on the head*'
        await interaction.response.send_message(msg)

    @app_commands.command()
    async def pats(self, interaction: discord.Interaction, member: discord.Member):
        if member.id == 1093034030745780286:
            msg = f'Wha- I\'m not patting myself!\n*pats {interaction.user.mention}*'
        else:
            msg = f'*pats {member.mention} on the head*'
        await interaction.response.send_message(msg)

    @app_commands.command()
    async def hug(self, interaction: discord.Interaction, member: discord.Member):
        if member.id == 1093034030745780286:
            msg = f'Wha- I\'m not huggin myself!\n*hugs {interaction.user.mention} tightly*'
        else:
            msg = f'*hugs {member.mention} gently*'
        await interaction.response.send_message(msg)

async def setup(bot):
    await bot.add_cog(Tests(bot))
