import discord
from discord import app_commands
from discord.ext import commands
from bot import PawBot

class verifiedRole(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    #Sauce of some of this amazing code: https://stackoverflow.com/questions/52210855/give-role-when-a-user-add-reaction-discord-py
    # @client.event
    # async def on_ready():
    #     Channel = client.get_channel(self.VERIFIED_CHANNEL)
    #     Moji = await Channel.send("Text")
    #     await Moji.add_reaction('✅') #:white_chek_mark:

    # @client.tree.command()
    # async def info(interaction: discord.Interaction, member: discord.Member):
    #     """Tells you some info about the member."""
    #     msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    #     await interaction.response.send_message(msg)

    @app_commands.command(name="verifiedtrigger")
    async def verifiedTrigger(self, interaction: discord.Interaction):
        if interaction.user.id == self.client.MY_USER_ID:
            msg = "By reacting to this message, you will gain access to the rest of the server and agree to our server rules."
            await interaction.response.send_message(msg)
            await msg.add_reaction('✅')
        else:
            channel = await interaction.user.create_dm()
            await channel.send(
            f'{interaction.user}! You are not allowed to run the `verifiedTrigger` command! Your attempt will be logged.'
            )
            channel = self.client.get_channel(self.client.VERIFIED_CHANNEL)
            await channel.send(
            f'NOT ALLOWED COMMAND USAGE ALERT! User: {interaction.user} (User ID: {interaction.user.id}) Violating command: `verifiedTrigger`'
            )
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction, user):
        Channel = self.client.get_channel(self.client.VERIFIED_CHANNEL)
        if reaction.message.channel.id != Channel.id:
            return
        if reaction.emoji == "✅":
            Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
            await user.add_roles(Role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction, user):
        Channel = self.client.get_channel(self.client.VERIFIED_CHANNEL)
        if reaction.message.channel.id != Channel.id:
            return
        if reaction.emoji == "✅":
            pass #The bot needs to give the reaction back to the user
            # Below is commented out, because the client shouldn't be able to unverify themselves
            #Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
            #await user.remove_roles(Role)

class reactionRoles(commands.Cog):
    def __init__(self, client):
        self.client: PawBot = client

    # The trigger is not properly set up...
    @app_commands.command(name="rolestrigger")
    async def rolesTrigger(self, interaction: discord.Interaction):
        if interaction.user.id == self.client.MY_USER_ID:
            msg = "BARK BARK BARK"
            await interaction.response.send_message(msg)
            await msg.add_reaction('✅')
        else:
            channel = await interaction.user.create_dm()
            await channel.send(
            f'{interaction.user}! You are not allowed to run the `verifiedTrigger` command! Your attempt will be logged.'
            )
            channel = self.client.get_channel(self.client.ROLES_CHANNEL)
            await channel.send(
            f'NOT ALLOWED COMMAND USAGE ALERT! User: {interaction.user} (User ID: {interaction.user.id}) Violating command: `verifiedTrigger`'
            )
    
    pass #"ROLES_CHANNEL" in "self"

async def setup(bot):
    await bot.add_cog(verifiedRole(bot))
    await bot.add_cog(reactionRoles(bot))
