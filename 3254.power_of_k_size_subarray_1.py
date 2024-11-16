from collections import deque
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans: list[int] = []
        if k == 1:
            return nums
        queue: deque[bool] = deque()
        current_sortedness = 0
        target_sortedness = k - 1
        for i in range(k - 1):
            if nums[i + 1] == nums[i] + 1:
                current_sortedness += 1
                queue.append(True)
            else:
                queue.append(False)

        right = k - 1
        while right < len(nums) - 1:
            if current_sortedness == target_sortedness:
                ans.append(nums[right])
            else:
                ans.append(-1)
            if queue.popleft():
                current_sortedness -= 1
            if nums[right + 1] == nums[right] + 1:
                current_sortedness += 1
                queue.append(True)
            else:
                queue.append(False)
            right += 1
        if current_sortedness == target_sortedness:
            ans.append(nums[right])
        else:
            ans.append(-1)
        return ans
