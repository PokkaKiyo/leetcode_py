from typing import Optional


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return False

        init = initialize(nums)
        if not init:
            return False
        smallest_so_far, upper, start = init
        lower = smallest_so_far
        for i in range(start, len(nums)):
            val = nums[i]
            if val > upper:
                return True
            if val == upper:
                lower = min(smallest_so_far, lower)
                continue

            assert val < upper

            if val > lower:
                upper = val
                lower = min(smallest_so_far, lower)
                continue
            elif val == lower:
                if smallest_so_far < lower:
                    upper = lower
                    lower = smallest_so_far
                continue

            assert val < lower

            if val > smallest_so_far:
                upper = val
                lower = smallest_so_far
                continue
            elif val == smallest_so_far:
                continue
            else:
                smallest_so_far = val
                continue

        return False


def initialize(nums: list[int]) -> Optional[tuple[int, int, int]]:
    smallest_so_far = nums[0]
    for i in range(1, len(nums)):
        val = nums[i]
        if val > smallest_so_far:
            return smallest_so_far, val, i + 1
        else:
            smallest_so_far = val
    return None
