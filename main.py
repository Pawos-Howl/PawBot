import os, discord
from discord.errors import NotFound
from discord.ext.commands import Cog
from discord.app_commands.errors import CommandNotFound as AppCommandNotFound, CommandInvokeError
# The following two lines break my code on windows. use on Mac (\n for spaces): from dotenv import load_dotenv \n load_dotenv()
from bot import PawBot
from utils import setupLogger
logger = setupLogger()

import platform # Check OS
if platform.system() == "Darwin": # MacOS
    from dotenv import load_dotenv
    load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
def setup(client):
    client.add_cog(Cog(client))
client = PawBot()

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error:Exception) -> None: # : discord.app_commands.AppCommandError
    print(f"main: {type(error)}")
    if isinstance(error, AppCommandNotFound): return
    if isinstance(error, NotFound): return
    if interaction.user.id == client.MY_USER_ID: 
        err_str = f"`{getattr(error, '__module__')}:  {error.args[0]}`"
        try:
            await interaction.response.send_message(err_str)
        except discord.errors.InteractionResponded:
            pass

    if isinstance(error, CommandInvokeError):
        #return
        logger.exception(error.__cause__)

    logger.exception(error)

@client.command()
async def hewwo(ctx, member: discord.member):
    await ctx.send(f'Hewwo {member}! How are you doing?')

#Might work in "tests" file
# @client.command()
# async def generalTest(ctx):
#     await ctx.send('STANDARD TEST:\nRETURNED TRUE. TEST SUCESSFUL.')

# @client.tree.command()
# async def info(interaction: discord.Interaction, member: discord.Member): # This is how you do slash commands; switched ctx for interaction
#     """Tells you some info about the member."""
#     msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
#     await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

client.run(TOKEN) # This ALWAYS is at the bottom of the file no matter what
