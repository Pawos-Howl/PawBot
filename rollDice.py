import discord, random
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class rolling(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @app_commands.command()
    async def roll(self, interaction: discord.Interaction, *, dice_sides: int, number_of_dice: int = 1, add: int = None, multiply: int = None):
        # null is there or else dice_sides doesn't appear
        """Rolling Commands: Sides of dice (required). Optional: number of dice; add; mutliply."""
        amount_of_dice = number_of_dice
        dice_add = add
        dice_multiply = multiply
        dice_sum = 0
        dice_rolls = []

        # "Rolls" the dice
        for i in range(amount_of_dice):
            randomNumber = random.randint(1, dice_sides)
            dice_rolls.append(randomNumber)
            dice_sum += randomNumber

        if add != None: dice_sum += add
        if multiply != None: dice_sum = int(dice_sum)*int(multiply)

        # Gives a "nice" looking output
        if len(dice_rolls) == 1 and dice_multiply == None and dice_add == None: return f'The random number is {dice_sum}'
        appendRoll = ''
        if dice_add != None: appendRoll += f'Added:{dice_add}; '
        if dice_multiply != None: appendRoll += f'Multiplied:{dice_multiply}; '
        if len(dice_rolls) == 1: appendRoll += f'Roll:{dice_rolls[0]}'
        if len(dice_rolls) >= 2: 
            rollsAppend = ''
            for i in range(0, len(dice_rolls)-1):
                rollsAppend += f'{dice_rolls[i]}, '
            rollsAppend += f'{dice_rolls[i+1]}'
            appendRoll += f'Rolls:{rollsAppend}'
        msg =  f'The result is {dice_sum}\n{appendRoll}'
        await interaction.response.send_message(msg)

async def setup(bot):
    await bot.add_cog(rolling(bot))