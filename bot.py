import discord, logging
from discord.ext.commands import Bot, CommandNotFound
from discord.app_commands.errors import CommandInvokeError

# Thank you Ovlic for the code
#\u001b[38;5;82;1m
log = logging.getLogger("PawBot.\u001b[38;5;82;1mBot\u001b[0m")

class PawBot(Bot):
    def __init__(self):
        # ↓↓↓ Personal opinion, some of these variables are only used in
        # specific cogs, just move them into that cog's __init__ function
        # instead of having them here. It will make it easier to read
        # and understand in the future.
        self.MY_GUILD = discord.Object(id=int(1023691852072886332)) # Set this to the guild ID you want to use slash commands
        self.MY_USER_ID =  discord.Object(id=int(979210001556070491))
        self.JOIN_AND_LEAVE_CHANNEL = discord.Object(id=int(1097030111125045279))
        self.VERIFIED_CHANNEL = discord.Object(id=int(1092923045427027998))
        self.ROLES_CHANNEL = discord.Object(id=int(1092923070211162133))
        self.DENIED_COMMAND_USAGE = discord.Object(id=int(1099002597253320706))
        self.STAFF_ALERTS_CHANNEL = discord.Object(id=int(1098338464321245224))
        # ↓↓↓ Also a good habit to do is to move your super inits to the bottom
        # of the __init__ function so you can initialize the other variables
        # first then get the rest of the stuff from the super init.
        super().__init__(intents=discord.Intents.all(),command_prefix="!paw ")

    async def on_ready(self): # All this function really needs to do is just say that its online, no need for any fancy stuff
        print("Bot is online!")

    async def on_command_error(self, ctx, ex):
        print(f"main.on_command_error: {type(ex)}")
        if isinstance(ex, CommandNotFound): return
        if ctx.author.id == self.MY_USER_ID: # Why not make this utils.owner_ids?
            err_str = f"`{getattr(ex, '__module__')}:  {ex.args[0]}`"
            await ctx.reply(err_str)
        if isinstance(ex, CommandInvokeError):
            log.exception(ex.__cause__)
        else:
            log.exception(ex)
        raise ex.__cause__ # Fixed repetition

    async def setup_hook(self):
        # for guild in self.guilds: 
        # If you want to sync all guilds dont loop like this Just load
        # them all at once with one command

        # Also one more thing, if you end up with many cogs (in the future)
        # you can make a folder called cogs and put all the cogs files in
        # there and then loop through all the files in that folder and load
        # them that way.

        # An example of this would be:
        # for filename in os.listdir("./cogs"):
        #     if filename.endswith(".py"):
        #         client.load_extension(f"cogs.{filename[:-3]}")
        #         print("Cog Loaded!")

        await self.load_extension('greetingCommands')
        await self.load_extension('JoinAndLeave')
        await self.load_extension('reactionRoles')
        await self.load_extension('info')
        await self.load_extension('affection')
        await self.load_extension('botDisable')
        await self.tree.sync() 
        # ↑↑↑ This may take some time to update, but if its your main bot
        # that wont be constantly rerun for testing then it should be fine.

        # One other thing, you could create a command that will sync the
        # commands instead since it won't be affected that much by rate limits
        # but make sure to set the permissions and visibility of it to only 
        # you or the other person/people that own the bot.

        # The command would look something like this:
        # @client.tree.command()
        ## You could also put a checker here if needed
        # async def sync(interaction: discord.Interaction):
        #    if interaction.user.id in utils.owner_ids:
        #       await interaction.response.send_message("Syncing commands...", ephemeral=True)
        #       await client.tree.sync()
        #       await interaction.edit_original_message(content="Synced commands!", ephemeral=True)
        #    else:
        #       await interaction.response.send_message("You are not allowed to run this command!", ephemeral=True)
        

        #Cog Imports
        # await self.load_extension('greetingCommands')
        # await self.load_extension('JoinAndLeave')
        # await self.load_extension('reactionRoles')
        # await self.load_extension('info')
        # await self.load_extension('affection')
        # await self.load_extension('botDisable')
        #Leave at the bottom
        # self.tree.copy_global_to(guild=self.MY_GUILD)
        # await self.tree.sync(guild=self.MY_GUILD)