import discord, random
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class rolling(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command()
    async def roll(self, interaction: discord.Interaction, number: int):
        randValue = random.randint(1, number)
        msg = f'The random number is {randValue}'
        await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

async def setup(bot):
    await bot.add_cog(rolling(bot))