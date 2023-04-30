import discord, os, logging
from discord.ext.commands import Bot, CommandNotFound
from discord.app_commands.errors import CommandInvokeError
from dotenv import load_dotenv
load_dotenv()

# Thank you Ovlic for the code
#\u001b[38;5;82;1m
log = logging.getLogger("PawBot.\u001b[38;5;82;1mBot\u001b[0m")

class PawBot(Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(),command_prefix="!paw ") # Do not set the command prefix to / since that is the default for slash commands
        self.MY_GUILD = discord.Object(id=int(os.getenv('DISCORD_GUILD'))) # Set this to the guild ID you want to use slash commands
        self.MY_USER_ID =  discord.Object(id=int(979210001556070491))
        self.JOIN_AND_LEAVE_CHANNEL = discord.Object(id=int(1097030111125045279))
        self.VERIFIED_CHANNEL = discord.Object(id=int(1092923045427027998))
        self.ROLES_CHANNEL = discord.Object(id=int(1092923070211162133))
        self.DENIED_COMMAND_USAGE = discord.Object(id=int(1099002597253320706))
        self.STAFF_ALERTS_CHANNEL = discord.Object(id=int(1098338464321245224))

    async def on_ready(self): # All this function really needs to do is just say that its online, no need for any fancy stuff
        print("Bot is online!")

    async def on_command_error(self, ctx, ex):
        print(f"main.on_command_error: {type(ex)}")
        if isinstance(ex, CommandNotFound): return
        if ctx.author.id == self.MY_USER_ID: 
            err_str = f"`{getattr(ex, '__module__')}:  {ex.args[0]}`"
            await ctx.reply(err_str)
        if isinstance(ex, CommandInvokeError):
            log.exception(ex.__cause__)
            raise ex.__cause__
        else:
            log.exception(ex)
            raise ex.__cause__

    async def setup_hook(self):
        #Cog Imports
        await self.load_extension('greetingCommands')
        await self.load_extension('JoinAndLeave')
        await self.load_extension('reactionRoles')
        await self.load_extension('tests')
        await self.load_extension('info')
        await self.load_extension('rollDice')
        await self.load_extension('affection')
        #await self.load_extension('botDisable') #NOT WORKING!!!
        #Leave at the bottom
        self.tree.copy_global_to(guild=self.MY_GUILD)
        await self.tree.sync(guild=self.MY_GUILD)