from discord.ext.commands import Bot

if __name__ == "__main__":

    bot = Bot(command_prefix="!")

    bot.load_extension("commands")
    bot.load_extension("listeners")

    bot.run("NjkzMjIzMjcwNjY4OTU5NzQ0.Xn58qA.qfC3YkOF60-7ULc9LAbrGioIGWc")



