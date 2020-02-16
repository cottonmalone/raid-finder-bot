from raidfinder.frames.xoro_shiro import *


def test_xoro_shiro_ctr():
    xs = XoroShiro(1000)
    assert xs.s0 == 1000
    assert xs.s1 == S1


def test_xoro_shiro_clone():
    x1 = XoroShiro(1)
    x2 = x1.clone()
    assert x1.s0 == x2.s0
    x2.next()
    assert x1.s0 != x2.s0


def test_xoro_shiro_next():
    x1 = XoroShiro(1)
    x1.next()
    assert x1.s0 == 3735617041806617178


def test_xoro_shiro_next_int():
    x1 = XoroShiro(1)
    assert x1.next_int(5, 10) == 4
    assert x1.next_int(5, 10, 1) == (4, 1)
