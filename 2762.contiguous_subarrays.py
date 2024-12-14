from collections import defaultdict, deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        window: deque[int] = deque()
        contents: defaultdict[int, int] = defaultdict(int)
        ans = 0

        def prune(num: int) -> None:
            valid_range = range(num - 2, num + 2 + 1)
            for i in range(len(window) - 1):
                if all(key in valid_range for key in contents):
                    return
                left = window.popleft()
                contents[left] -= 1
                if contents[left] == 0:
                    del contents[left]

        for num in nums:
            contents[num] += 1
            window.append(num)
            prune(num)
            ans += len(window)

        return ans

    def continuousSubarrays2(self, nums: list[int]) -> int:
        window_left = 0
        contents: defaultdict[int, int] = defaultdict(int)
        ans = 0

        def prune(num: int, window_left: int, window_right: int) -> int:
            valid_range = range(num - 2, num + 2 + 1)
            while window_left < window_right:
                if all(key in valid_range for key in contents):
                    break
                left = nums[window_left]
                contents[left] -= 1
                if contents[left] == 0:
                    del contents[left]
                window_left += 1
            return window_left

        for idx, num in enumerate(nums):
            contents[num] += 1
            window_left = prune(num, window_left, idx)
            ans += idx - window_left + 1

        return ans
