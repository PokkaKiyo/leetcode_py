from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        peak = max(candies) - extraCandies
        return [candy >= peak for candy in candies]
