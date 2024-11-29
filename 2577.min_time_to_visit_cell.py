import heapq
from collections import defaultdict
from typing import List, NamedTuple


class Element(NamedTuple):
    time: int
    row: int
    col: int


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] >= 2 and grid[1][0] >= 2:
            return -1

        n = len(grid)
        m = len(grid[0])
        visited = defaultdict(bool)

        pq: list[Element] = []
        pq.append(Element(0, 0, 0))

        ans = pq[0]  # stub
        while pq:
            ele = heapq.heappop(pq)
            if ele.row == n - 1 and ele.col == m - 1:
                ans = ele
                break
            if visited[(ele.row, ele.col)]:
                continue
            visited[(ele.row, ele.col)] = True
            process_neighbours(ele.time, ele.row, ele.col, grid, pq)

        return ans.time


def process_neighbours(
    time: int,
    row: int,
    col: int,
    grid: list[list[int]],
    pq: list[Element],
):
    # left
    if row - 1 >= 0:
        next_time = grid[row - 1][col]
        if next_time <= time + 1:
            heapq.heappush(pq, (Element(time + 1, row - 1, col)))
        else:
            diff = next_time - (time + 1)
            if diff % 2 == 0:
                heapq.heappush(pq, (Element(next_time, row - 1, col)))
            else:
                heapq.heappush(pq, (Element(next_time + 1, row - 1, col)))

    # right
    if row + 1 < len(grid):
        next_time = grid[row + 1][col]
        if next_time <= time + 1:
            heapq.heappush(pq, (Element(time + 1, row + 1, col)))
        else:
            diff = next_time - (time + 1)
            if diff % 2 == 0:
                heapq.heappush(pq, (Element(next_time, row + 1, col)))
            else:
                heapq.heappush(pq, (Element(next_time + 1, row + 1, col)))
    # top
    if col - 1 >= 0:
        next_time = grid[row][col - 1]
        if next_time <= time + 1:
            heapq.heappush(pq, (Element(time + 1, row, col - 1)))
        else:
            diff = next_time - (time + 1)
            if diff % 2 == 0:
                heapq.heappush(pq, (Element(next_time, row, col - 1)))
            else:
                heapq.heappush(pq, (Element(next_time + 1, row, col - 1)))

    # btm
    if col + 1 < len(grid[0]):
        next_time = grid[row][col + 1]
        if next_time <= time + 1:
            heapq.heappush(pq, (Element(time + 1, row, col + 1)))
        else:
            diff = next_time - (time + 1)
            if diff % 2 == 0:
                heapq.heappush(pq, (Element(next_time, row, col + 1)))
            else:
                heapq.heappush(pq, (Element(next_time + 1, row, col + 1)))
