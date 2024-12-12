from heapq import heapify, heappop, heappush
from math import floor, sqrt


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap: list[int] = []
        total = 0
        for gift in gifts:
            total += gift
            heappush(heap, -gift)

        for i in range(k):
            out = heappop(heap) * -1
            remaining = floor(sqrt(out))
            removed = out - remaining
            assert removed >= 0
            total -= removed
            heappush(heap, -remaining)
        return total

    def micro_optimized(self, gifts: list[int], k: int):
        heap = [-gift for gift in gifts]
        heapify(heap)

        for i in range(k):
            remaining = floor(sqrt(heappop(heap) * -1))
            heappush(heap, -remaining)

        return sum(heap) * -1
