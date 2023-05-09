import discord, random
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class rolling(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command()
    async def roll(self, interaction: discord.Interaction, number: int, add: int = None):
        randValue = random.randint(1, number)
        if add == None: msg = f'The random number is {randValue}'
        if add != None: msg = f'The random number is {randValue+add}.\nWhich accounts for an added {add}, and the original number was {randValue}'
        await interaction.response.send_message(msg)

async def setup(bot):
    await bot.add_cog(rolling(bot))