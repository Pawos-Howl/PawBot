from discord.ext import commands
from bot import PawBot

class JoinAndLeave(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #await self.client.get_channel(self.client.JOIN_AND_LEAVE_CHANNEL).send(f"{member.name} has joined")
        channel = await member.create_dm() # Create the channel and set it to a variable instead
        await channel.send(
        f'Hewwo {member.name}! Welcome to the Pawos Howl Gang! This bot was coded by Paw (with some help from friends). Have fun and enjoy your stay! -Pawos Howl'
        )
        await self.client.get_channel(self.client.JOIN_AND_LEAVE_CHANNEL).send(f"{member} has joined")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #pass #temporary
        await self.client.get_channel(self.client.JOIN_AND_LEAVE_CHANNEL).send(f"{member} has left")

async def setup(bot):
    await bot.add_cog(JoinAndLeave(bot))
