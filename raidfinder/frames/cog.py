from discord.ext import commands
from .frame_data import *
from .frame_card import *


class FrameDataCog(commands.Cog, name="Raid Info"):
    @commands.command(name="getshinyframes")
    async def get_shiny_frames(self, ctx, seed, max_count=10000, n_best_ivs=4):
        """
        Get shiny frames for the given seed.

        Args:
            seed: The den's seed.
            max_count (int): The number of frames to search.
            n_best_ivs (int): The IV count for the stats.
        """
        data = get_shiny_frames(int(seed, 16), max_count, n_best_ivs)

        await ctx.send(
            embed=get_card_for_shiny_frames(seed, data, max_count, n_best_ivs)
        )
