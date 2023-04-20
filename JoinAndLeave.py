from discord.ext import commands
from bot import PawBot

class JoinAndLeave(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    # OS path of ENV "os.getenv('GUILD_JOIN_AND_LEAVE_CHANNEL_ID')"
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(self.JOIN_AND_LEAVE_CHANNEL).send(f"{member.name} has joined")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(self.JOIN_AND_LEAVE_CHANNEL).send(f"{member.name} has left")

async def setup(bot):
    await bot.add_cog(JoinAndLeave(bot))
