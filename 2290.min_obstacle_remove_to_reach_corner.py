import collections
import heapq
from collections import defaultdict, deque
from typing import List, NamedTuple


class Element(NamedTuple):
    dist: int
    row: int
    col: int


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """Dijkstra."""
        pq: list[Element] = []
        pq.append(Element(grid[0][0], 0, 0))
        visited: defaultdict[tuple[int, int], bool] = defaultdict(bool)

        n = len(grid)
        m = len(grid[0])

        while pq[0].row != n - 1 or pq[0].col != m - 1:
            pop = heapq.heappop(pq)
            if visited[(pop.row, pop.col)]:
                continue
            visited[(pop.row, pop.col)] = True
            if pop.row > 0:
                heapq.heappush(
                    pq,
                    Element(pop.dist + grid[pop.row - 1][pop.col], pop.row - 1, pop.col),
                )
            if pop.row < n - 1:
                heapq.heappush(
                    pq,
                    Element(pop.dist + grid[pop.row + 1][pop.col], pop.row + 1, pop.col),
                )
            if pop.col > 0:
                heapq.heappush(
                    pq,
                    Element(pop.dist + grid[pop.row][pop.col - 1], pop.row, pop.col - 1),
                )
            if pop.col < m - 1:
                heapq.heappush(
                    pq,
                    Element(pop.dist + grid[pop.row][pop.col + 1], pop.row, pop.col + 1),
                )

        return pq[0].dist
