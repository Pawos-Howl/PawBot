import os
#from discord.ext.commands.cog import Cog
from discord.ext import commands

# from bot import PawBot

# client = PawBot()
# def setup(client):
#     client.add_cog(Cog(client))

class JoinAndLeave(commands.Cog):
    # OS path of ENV "os.getenv('GUILD_JOIN_AND_LEAVE_CHANNEL_ID')"
    @commands.Cog.listener()
    async def on_member_join(member):
        await client.get_channel(os.getenv('JOIN_AND_LEAVE_CHANNEL')).send(f"{member.name} has joined")

    @commands.Cog.listener()
    async def on_member_remove(member):
        await client.get_channel(os.getenv('JOIN_AND_LEAVE_CHANNEL')).send(f"{member.name} has left")

    # OS path of ENV "os.getenv('GUILD_JOIN_AND_LEAVE_CHANNEL_ID')"
    # @client.event
    # async def on_member_join(member):
    #     await client.get_channel(idchannel).send(f"{member.name} has joined")

    # @client.event
    # async def on_member_remove(member):
    #     await client.get_channel(idchannel).send(f"{member.name} has left")
