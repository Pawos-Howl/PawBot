import discord
from discord.errors import NotFound
from discord.ext.commands import Cog
from discord.app_commands.errors import CommandNotFound as AppCommandNotFound, CommandInvokeError
from dotenv import load_dotenv
from os import getenv # if you use this for only one thing just import the function instead.
from bot import PawBot
from utils import setupLogger

load_dotenv() # Just cleaning up the order of things.
logger = setupLogger()
TOKEN = getenv('DISCORD_TOKEN')

client = PawBot()

# Why is this here? This is for a cog and doesnt work here.
def setup(client):
    client.add_cog(Cog(client))

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error:Exception) -> None: # : discord.app_commands.AppCommandError
    print(f"main: {type(error)}")
    if isinstance(error, AppCommandNotFound): return
    if isinstance(error, NotFound): return
    if interaction.user.id == client.MY_USER_ID: # Why not make this utils.owner_ids?
        err_str = f"`{getattr(error, '__module__')}:  {error.args[0]}`"
        try:
            await interaction.response.send_message(err_str)
        except discord.errors.InteractionResponded:
            pass

    if isinstance(error, CommandInvokeError):
        #return
        logger.exception(error.__cause__)

    logger.exception(error)

# @client.command()
# async def hewwo(ctx, member: discord.member):
#     await ctx.send(f'Hewwo {member}! How are you doing?')

client.run(TOKEN) # This ALWAYS is at the bottom of the file no matter what
