import collections
from enum import Enum, auto
from .xoro_shiro import XoroShiro

FRAME_MAX_INT = 0xFFFFFFFF

FrameData = collections.namedtuple("FrameData", ["type", "ivs", "ability"])


class ShinyType(Enum):
    NONE = auto()
    STAR = auto()
    SQUARE = auto()


def get_shiny_xor(val):
    return (val >> 16) ^ (val & 0xFFFF)


def get_shiny_type(pid, sidtid):
    p = get_shiny_xor(pid)
    t = get_shiny_xor(sidtid)

    if p == t:
        return ShinyType.SQUARE

    if (p ^ t) < 0x10:
        return ShinyType.STAR

    return ShinyType.NONE


def get_ivs_for_frame(rng, n_best_ivs):

    ivs = [-1] * 6
    count, n_ivs, offset = 0, n_best_ivs, -n_best_ivs

    while count < n_ivs:
        stat, offset = rng.next_int(7, 6, offset)

        if ivs[stat] == -1:
            ivs[stat] = 31
            count += 1

    for x in range(0, 6):
        if ivs[x] != 31:
            ivs[x] = rng.next_int(31)

    return ivs


def get_ability(rng, n_best_ivs):
    if n_best_ivs > 3:
        return rng.next_int(3, 3) + 1

    return rng.next_int(1) + 1


def get_frame_data(rng: XoroShiro, n_best_ivs):
    # ignore characteristics
    _ = rng.next_int(FRAME_MAX_INT, FRAME_MAX_INT)

    sidtid = rng.next_int(FRAME_MAX_INT, FRAME_MAX_INT)
    pid = rng.next_int(FRAME_MAX_INT, FRAME_MAX_INT)

    shiny_type = get_shiny_type(pid, sidtid)

    return FrameData(
        type=shiny_type,
        ivs=get_ivs_for_frame(rng, n_best_ivs),
        ability=get_ability(rng, n_best_ivs),
    )


def get_shiny_frames(seed, max_count, n_best_ivs):
    frames = []

    rng = XoroShiro(seed)

    for i in range(1, max_count + 1):
        frame = get_frame_data(rng.clone(), n_best_ivs)

        if frame.type != ShinyType.NONE:
            frames.append((i, frame))
            print((i, frame))

        rng.next_frame()

    return frames


def get_data_for_n_frame(seed, n_frame, n_best_ivs):
    rng = XoroShiro(seed)

    [rng.next_frame() for i in range(n_frame - 1)]

    return get_frame_data(rng.clone(), n_best_ivs)
