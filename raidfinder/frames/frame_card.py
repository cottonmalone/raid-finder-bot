import discord

SHINY_TYPE_MAP = {"STAR": "⭐", "SQUARE": "🔸"}


def get_ivs_string(ivs):
    return "/".join(map(lambda x: f"{x: >2}", ivs))


def get_shiny_type(type):
    return SHINY_TYPE_MAP.get(type.name, "None")


def get_card_for_shiny_frames(seed, frames, max_count, n_best_ivs):

    if len(frames) == 0:
        return discord.Embed.from_dict(
            dict(
                title=f"Get Shiny Frames",
                description=f"There are **no shiny frames** below {max_count}.",
                fields=[{"name": "Seed", "value": f"```fix\n{seed}```"}],
            )
        )

    frame_count, shiny, ivs = [], [], []

    for idx, data in frames:
        frame_count.append(f"{idx: >5}")
        shiny.append(get_shiny_type(data.type))
        ivs.append(get_ivs_string(data.ivs))

    frame_count = "\n".join(frame_count)
    shiny = "\n".join(shiny)
    ivs = "\n".join(ivs)

    return discord.Embed.from_dict(
        dict(
            title=f"Get Shiny Frames",
            fields=[
                {"name": "Seed", "value": f"```fix\n{seed}```"},
                {"name": "Frame", "value": f"```fix\n{frame_count}```", "inline": True},
                {"name": "Shiny", "value": f"```{shiny}```", "inline": True},
                {"name": "IVs", "value": f"```py\n{ivs}```", "inline": True},
            ],
            footer={"text": f"* IVs shown are for IV count of {n_best_ivs}"},
        )
    )
