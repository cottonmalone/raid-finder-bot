import pytest
from raidfinder.frames.xoro_shiro import XoroShiro
from raidfinder.frames.frame_data import *


@pytest.mark.parametrize(
    "seed,n_best_ivs,expected_data",
    [
        (
            "2e6327d13bb66b32",
            1,
            FrameData(type=ShinyType.NONE, ivs=[20, 31, 25, 21, 17, 9], ability=1),
        ),
        (
            "2e6327d13bb66b32",
            2,
            FrameData(type=ShinyType.NONE, ivs=[25, 31, 21, 17, 31, 9], ability=1),
        ),
        (
            "2e6327d13bb66b32",
            3,
            FrameData(type=ShinyType.NONE, ivs=[17, 31, 9, 4, 31, 31], ability=1),
        ),
        (
            "2e6327d13bb66b32",
            4,
            FrameData(type=ShinyType.NONE, ivs=[31, 31, 14, 10, 31, 31], ability=3),
        ),
        (
            "7ba2221fe04db02e",
            1,
            FrameData(type=ShinyType.STAR, ivs=[2, 31, 4, 19, 29, 7], ability=2),
        ),
        (
            "7ba2221fe04db02e",
            4,
            FrameData(type=ShinyType.STAR, ivs=[29, 31, 31, 31, 31, 7], ability=3),
        ),
        (
            "b93ffe0fa2528987",
            1,
            FrameData(type=ShinyType.SQUARE, ivs=[31, 3, 28, 16, 10, 9], ability=2),
        ),
        (
            "b93ffe0fa2528987",
            4,
            FrameData(type=ShinyType.SQUARE, ivs=[31, 9, 31, 31, 31, 19], ability=2),
        ),
    ],
)
def test_frame_data_get_frame_data(seed, n_best_ivs, expected_data):
    assert get_frame_data(XoroShiro(int(seed, 16)), n_best_ivs) == expected_data
