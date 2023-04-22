import discord
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class Info(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command(name="info")
    async def info(interaction: discord.Interaction, member: discord.Member): # This is how you do slash commands; switched ctx for interaction
        """Tells you some info about the member."""
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

async def setup(bot):
    await bot.add_cog(Info(bot))
