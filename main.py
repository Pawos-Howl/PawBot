import os, discord
# The following two lines break my code on windows. use on Mac
#from dotenv import load_dotenv
#load_dotenv()
# Directory Inputs
#import puppyTime
from bot import PawBot

TOKEN = os.getenv('DISCORD_TOKEN')
# You dont need GUILD or intents here because you already did that in your bot file

bot = PawBot() # Move this to the top

@bot.event
async def on_member_join(member):
    channel = await member.create_dm() # Create the channel and set it to a variable instead
    await channel.send(
        f'Hewwo {member.name}! Welcome to the Pawos Howl Gang! Please read the rules and get your roles. This bot was coded by Paw herself (with a little help from some friends). Have fun and enjoy your stay! -Pawos Howl'
        )

@bot.event
async def on_message(message):
    ## Bot triggering itself protection
    if message.author == bot.user: return
    if message == 'hewwo':
        await message.channel.send("hewwo")
    # Catchall is not needed
    await bot.process_commands(message)


@bot.command()
async def generalTest(ctx):
    await ctx.send('STANDARD TEST:\nRETURNED TRUE. TEST SUCESSFUL.')

@bot.tree.command()
async def info(interaction: discord.Interaction, member: discord.Member): # This is how you do slash commands; switched ctx for interaction
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await interaction.response.send_message(msg) # Instead of ctx.send, use interaction.response.send_message

bot.run(TOKEN) # This ALWAYS is at the bottom of the file no matter what