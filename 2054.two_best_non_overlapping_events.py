from bisect import bisect_right
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])

        maximum: list[int] = []
        best = events[-1][2]
        for event in reversed(events):
            best = max(event[2], best)
            maximum.append(best)

        best = 0
        for idx, event in enumerate(events):
            _start, end, val = event
            right = bisect_right(events, end, idx + 1, key=lambda x: x[0])
            if right >= len(events):
                solution = 0
            else:
                solution = maximum[len(events) - 1 - right]
            best = max(best, val + solution)

        return best