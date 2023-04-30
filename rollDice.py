import discord, random
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class rolling(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command()
    async def randint(self, interaction: discord.Interaction, number: int, number2: int = None):
        if number2 != None:
            randValue = random.randint(number2, number)
        else:
            randValue = random.randint(1, number)
        msg = f'The random number is {randValue}'
        await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

    @app_commands.command()
    async def roll(self, interaction: discord.Interaction, number: int):
        randValue = random.randint(1, number)
        msg = f'The random number is {randValue}'
        await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

    @app_commands.command()
    async def rolls(self, interaction: discord.interactions, value: str):
        pass #take an input, seperate it, and do stuff with it. (ex: 4d20 would roll 4 D20s)

async def setup(bot):
    await bot.add_cog(rolling(bot))