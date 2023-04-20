import os, discord
from discord.ext.commands import Cog
# The following two lines break my code on windows. use on Mac (\n for spaces): from dotenv import load_dotenv \n load_dotenv()
from bot import PawBot
import platform # Check OS

if platform.system() == "Darwin": # MacOS
    from dotenv import load_dotenv
    load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
def setup(client):
    client.add_cog(Cog(client))
client = PawBot()

@client.event
async def on_member_join(member):
    channel = await member.create_dm() # Create the channel and set it to a variable instead
    await channel.send(
        f'Hewwo {member.name}! Welcome to the Pawos Howl Gang! This client was coded by Paw (with some help from friends). Have fun and enjoy your stay! -Pawos Howl'
        )
    
# The following lines do not work correctly. Error with needing to have clienth CTX and Message be first in the order
#@client.event
#async def on_message(ctx, message: discord.message, *, member: discord.member):
#    ## client triggering itself protection
#    if message.author == client.user: return
#    elif message == 'hewwo':
#        #await message.channel.send("hewwo")
#        await ctx.channel.send(f"hewwo {member}~ How are ya?")
#    # Catchall is not needed
#    #await client.process_commands(message)

@client.command()
async def hewwo(ctx, member: discord.member):
    await ctx.send(f'Hewwo {member}! How are you doing?')

@client.command()
async def generalTest(ctx):
    await ctx.send('STANDARD TEST:\nRETURNED TRUE. TEST SUCESSFUL.')

@client.tree.command()
async def info(interaction: discord.Interaction, member: discord.Member): # This is how you do slash commands; switched ctx for interaction
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

client.run(TOKEN) # This ALWAYS is at the bottom of the file no matter what
