from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack: list[tuple[int, int]] = []

        ans: list[int] = [0] * len(prices)
        # ans = prices  # we can actually use the prices arr directly

        for idx, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                original_price, position = stack.pop()
                ans[position] = original_price - price
            stack.append((price, idx))

        # if we used the prices directly as the ans array, we don't need this step
        for price, position in stack:
            ans[position] = price

        return ans

    def finalPrices2(self, prices: List[int]) -> List[int]:
        stack: list[int] = []  # the better answer stores the idx directly

        ans: list[int] = prices[:]  # create a copy of prices
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                position = stack.pop()
                ans[position] = prices[position] - price
            stack.append(idx)

        return ans
