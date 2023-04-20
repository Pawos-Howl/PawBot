import discord, os
#from discord.ext.commands.cog import Cog
from discord.ext import commands

import platform # Check OS

if platform.system() == "Darwin": # MacOS
    from dotenv import load_dotenv
    load_dotenv()

# from bot import PawBot

# client = PawBot()
# def setup(client):
#     client.add_cog(Cog(client))

class verifiedRole(commands.Cog):
    #Sauce of some of this amazing code: https://stackoverflow.com/questions/52210855/give-role-when-a-user-add-reaction-discord-py
    # @client.event
    # async def on_ready():
    #     Channel = client.get_channel(os.getenv('VERIFIED_CHANNEL'))
    #     Moji = await Channel.send("Text")
    #     await Moji.add_reaction('✅') #:white_chek_mark:

    # @client.tree.command()
    # async def info(interaction: discord.Interaction, member: discord.Member):
    #     """Tells you some info about the member."""
    #     msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    #     await interaction.response.send_message(msg)
    async def verifiedTrigger():
        Channel = client.get_channel(os.getenv('VERIFIED_CHANNEL'))
        Moji = await Channel.send("TEXT")
        await Moji.add_reaction('✅')
    @commands.Cog.event
    async def on_reaction_add(reaction, user):
        Channel = client.get_channel(os.getenv('VERIFIED_CHANNEL'))
        if reaction.message.channel.id != Channel.id:
            return
        if reaction.emoji == "✅":
            Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
            await user.add_roles(Role)
    @commands.Cog.event
    async def on_reaction_remove(reaction, user):
        Channel = client.get_channel(os.getenv('VERIFIED_CHANNEL'))
        if reaction.message.channel.id != Channel.id:
            return
        if reaction.emoji == "✅":
            Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
            await user.remove_roles(Role)

class reactionRoles(commands.Cog):
    pass #"ROLES_CHANNEL" in .env
