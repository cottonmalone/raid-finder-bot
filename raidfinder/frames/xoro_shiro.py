import sys

S1 = 0x82A2B175229D6A5B
MAX_INT = 0xFFFFFFFFFFFFFFFF


def rotl(x, k):
    return ((x << k) | (x >> (64 - k))) & MAX_INT


class XoroShiro:
    def __init__(self, seed):
        self.s0 = seed
        self.s1 = S1

    def next(self):
        result = (self.s0 + self.s1) & MAX_INT

        self.s1 ^= self.s0
        self.s0 = rotl(self.s0, 24) ^ self.s1 ^ ((self.s1 << 16) & MAX_INT)
        self.s1 = rotl(self.s1, 37)

        return result

    def next_int(self, mask, max_num=sys.maxsize, offset=None):
        result = self.next() & mask
        while result >= max_num:
            result = self.next() & mask
            if offset is not None:
                offset += 1

        if offset is not None:
            return result, offset

        return result

    def next_frame(self):
        self.s0 = (self.s0 + self.s1) & MAX_INT

    def clone(self):
        return XoroShiro(self.s0)
