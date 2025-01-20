import itertools


class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        arr = list(itertools.accumulate(height, max))

        right = 0
        for h, left in zip(reversed(height), reversed(arr)):
            ans += max(0, min(left, right) - h)
            right = max(right, h)

        return ans
