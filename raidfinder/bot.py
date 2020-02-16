import discord.ext.commands
from .embed import create_embed


class RaidFinderBot(discord.ext.commands.Bot):
    def __init__(self):
        super().__init__("$")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")


def create_bot():
    bot = RaidFinderBot()

    @bot.command()
    async def logout(ctx):
        # create bot card
        await ctx.send(embed=create_embed(description="Logging out..."))
        # logout
        await bot.logout()

    return bot
