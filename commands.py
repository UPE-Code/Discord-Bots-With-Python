from discord.ext.commands import Bot, Cog, command
import asyncio
import random

class BaseCommands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="ping")
    async def ping_pong(self, ctx):
        await ctx.send("ping!")

    @command(name="flip")
    async def flip_coin(self, ctx):
        coin = ["Heads!", "Tails!"]
        await ctx.send("{} {}".format(ctx.author.mention, random.choice(coin)))
        #@user random coin side

    @command(name="roll")
    async def roll_die(self, ctx, num_sides=6):
        await ctx.send("{} I rolled a {}".format(ctx.author.mention, random.randint(1, num_sides)))

    @command(name="sarcasm")
    async def spongebob_sarcasm(self, ctx, *args): # args = ["testing", "this", "message"]
        message = " ".join(args)
        sarcastic = ""
        for s in message:
            r = random.randint(0, 1)
            if r == 0:
                sarcastic += s.lower()
            else:
                sarcastic += s.upper()
        await ctx.send(sarcastic)
        
def setup(bot):
    bot.add_cog(BaseCommands(bot))
    print("Cog loaded: BaseCommands")

        