from itertools import pairwise


class Solution:
    def check(self, nums: list[int]) -> bool:
        rotated = False
        for i, j in pairwise(nums):
            if i > j:
                if rotated:
                    return False
                rotated = True
        if not rotated:
            return True
        return nums[-1] <= nums[0]
