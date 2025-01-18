import itertools


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return max([0, *itertools.accumulate(gain)])
