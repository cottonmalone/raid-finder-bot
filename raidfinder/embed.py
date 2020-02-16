import discord


REPO_URL = "https://github.com/cottonmalone/raid-finder-bot"

DEFAULT_EMBED_PARAMETERS = {
    "url": REPO_URL,
    "footer": {"text": "RaidFinder bot from cotton.malone"},
    "author": {"name": "RaidFinder", "url": REPO_URL},
}


def create_embed(**kwargs):
    return discord.Embed.from_dict({**kwargs, **DEFAULT_EMBED_PARAMETERS})
