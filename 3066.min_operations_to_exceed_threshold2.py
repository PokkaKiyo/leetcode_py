from heapq import heapify, heappop, heappushpop


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums[0] < k and len(nums) >= 2:
            heappushpop(nums, (heappop(nums) << 1) + nums[0])
            ans += 1
        return ans
