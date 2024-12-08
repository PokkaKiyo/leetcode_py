from bisect import bisect_right
from heapq import heappop, heappush
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
        prev_end, prev_val = -1, -1
        for idx, event in enumerate(events):
            _start, end, val = event

            if val <= prev_val and end >= prev_end:
                continue

            right = bisect_right(events, end, idx + 1, key=lambda x: x[0])
            if right >= len(events):
                solution = 0
            else:
                solution = maximum[len(events) - 1 - right]
            best = max(best, val + solution)

            prev_val = val
            prev_end = end

        return best

    def maxTwoEvents2(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])

        best = 0
        max_in_front = 0
        pq: list[tuple[int, int]] = []

        for event in events:
            start, end, val = event
            # look in front and see if any end times are earlier than start time
            while pq and pq[0][0] < start:
                end_, val_ = heappop(pq)
                max_in_front = max(max_in_front, val_)
            best = max(best, max_in_front + val)

            # we only need to push the new event to the stack
            # all previous events, we only cared about their largest val,
            # which has been encoded in "max_in_front"
            heappush(pq, (end, val))

        return best
