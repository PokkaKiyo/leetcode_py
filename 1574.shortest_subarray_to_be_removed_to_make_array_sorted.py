import functools
from itertools import pairwise
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = len(arr)
        for idx, (x, y) in enumerate(pairwise(arr)):
            if x > y:
                left = idx
                break
        if left == len(arr):
            return 0

        right = 0
        for idx, (x, y) in enumerate(pairwise(reversed(arr))):
            if y > x:
                right = len(arr) - 1 - idx
                break

        @functools.cache
        def dp(left, right):
            if right == len(arr) or left < 0 or arr[left] <= arr[right]:
                return right - left - 1
            return min(dp(left - 1, right), dp(left, right + 1))

        return dp(left, right)
