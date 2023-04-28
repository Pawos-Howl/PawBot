import discord
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class Info(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command()
    async def info(self, interaction: discord.Interaction, member: discord.Member): # This is how you do slash commands; switched ctx for interaction
        """Tells you some info about the member."""
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

    @commands.command()
    async def sourceCode(self, ctx, member: discord.Member):
        await ctx.send(f'Well, {member.name}, I am open source! You can find my souce code at https://github.com/Pawos-Howl/PawBot/. Have fun with the source code!')

async def setup(bot):
    await bot.add_cog(Info(bot))
