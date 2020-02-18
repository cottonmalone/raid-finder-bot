import discord.ext.commands
from .bot_cog import RaidFinderBotCog
from .frames.cog import FrameDataCog


class RaidFinderBot(discord.ext.commands.Bot):
    def __init__(self):
        super().__init__("$")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")


def create_bot():
    bot = RaidFinderBot()

    bot.add_cog(RaidFinderBotCog(bot))
    bot.add_cog(FrameDataCog())

    return bot
