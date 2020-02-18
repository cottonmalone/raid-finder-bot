from discord.ext import commands
from .embed import create_embed


class RaidFinderBotCog(commands.Cog, name="Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def logout(self, ctx):
        """
        Logout & shutdown bot.
        """
        await ctx.send(embed=create_embed(description="Logging out..."))
        # logout
        await self.bot.logout()
