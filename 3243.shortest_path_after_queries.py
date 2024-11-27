from typing import List


class Adjacency:
    __slots__ = ("min_distance", "adjacent")

    def __init__(self, min_distance: int, adjacent: list[int]) -> None:
        self.min_distance = min_distance
        self.adjacent = adjacent


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        assert n >= 3

        result: list[int] = []
        distances: list[Adjacency] = []
        for i in range(n - 1):
            distances.append(Adjacency(min_distance=(n - i - 1), adjacent=[i + 1]))
        distances.append(Adjacency(min_distance=0, adjacent=[]))

        for query_idx, (u, v) in enumerate(queries):
            distances[u].adjacent.append(v)
            for i in reversed(range(u + 1)):
                update_distances(distances, i)
            result.append(distances[0].min_distance)

        return result


def update_distances(distances: list[Adjacency], u: int):
    mapping: dict[int, int] = {}
    for v in distances[u].adjacent:
        mapping[v] = distances[v].min_distance
    distances[u].min_distance = min(mapping.values()) + 1


print(Solution().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))
