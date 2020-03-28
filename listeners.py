from discord import version_info, __version__
from discord.ext.commands import Cog
import asyncio

class EventListeners(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_connect(self):
       print("Connected to Discord!") 

    @Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")
        print("Version: " + __version__)
        print("Version Info: " + str(version_info))
    
    @Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            if message.content.lower().startswith("i'm"):
                await message.channel.send("Hi {}! I'm UPE-CODE Bot".format(message.content[4:]))

def setup(bot):
    bot.add_cog(EventListeners(bot))
    print("Cog loaded: EventListeners")