from discord.ext.commands import Cog, CheckFailure, MissingRequiredArgument, TooManyArguments
import asyncio

class CommandErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = "Ignoring {} in command '{}' by user {}"

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            print(self.message.format(ctx.command, ctx.author.id))
        elif isinstance(error, MissingRequiredArgument):
            print(self.message.format(ctx.command, ctx.author.id))
        elif isinstance(error, TooManyArguments):
            print(self.message.format(ctx.command, ctx.author.id))
    
def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
    print("Loaded Cog: CommandErrorHandler")
