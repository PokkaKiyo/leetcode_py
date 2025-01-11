import operator
from itertools import accumulate
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = list(accumulate(nums, func=operator.mul))
        suffixes = list(reversed(list(accumulate(reversed(nums), func=operator.mul))))
        ans = []
        for idx, _ in enumerate(nums):
            prefix = 1 if idx - 1 < 0 else prefixes[idx - 1]
            suffix = 1 if idx + 1 >= len(nums) else suffixes[idx + 1]
            ans.append(prefix * suffix)
        return ans
