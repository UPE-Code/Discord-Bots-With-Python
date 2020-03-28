from discord.ext.commands import Bot

if __name__ == "__main__":

    bot = Bot(command_prefix="!")

    bot.load_extension("commands")
    bot.load_extension("listeners")

    bot.run("BOT-TOKEN-HERE")



