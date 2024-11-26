class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        is_unbeaten = [True] * n
        count = n
        for edge in edges:
            winner, loser = edge
            if is_unbeaten[loser]:
                count -= 1
            is_unbeaten[loser] = False
        if count == 1:
            return is_unbeaten.index(True)
        return -1

    def findChampion_with_indegree(self, n: int, edges: list[list[int]]) -> int:
        degrees = [0] * n
        for edge in edges:
            winner, loser = edge
            degrees[loser] += 1

        champions = []
        for idx, deg in enumerate(degrees):
            if deg == 0:
                champions.append(idx)
        if len(champions) == 1:
            return champions[0]
        return -1
