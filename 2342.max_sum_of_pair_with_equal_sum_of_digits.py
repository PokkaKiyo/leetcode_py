class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        ans = -1
        nums.sort(reverse=True)
        sums: dict[int, int] = {}
        largest = nums[0]
        for num in nums:
            if (largest + num) <= ans:
                return ans
            sum_of_digits = self.calculate_sum_of_digits(num)
            if (partner := sums.get(sum_of_digits)) is None:
                sums[sum_of_digits] = num
            else:
                ans = max(ans, partner + num)
                if num > partner:
                    sums[sum_of_digits] = num
        return ans

    def calculate_sum_of_digits(self, num: int) -> int:
        total = 0
        while num > 0:
            num, remainder = divmod(num, 10)
            total += remainder
        return total
