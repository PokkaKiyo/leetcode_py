from bisect import insort
from collections import defaultdict
from heapq import heappop, heappush


class NumberContainersSortedList:
    __slots__ = ("containers", "indices_map")

    def __init__(self) -> None:
        self.containers: dict[int, int] = defaultdict(int)
        self.indices_map: dict[int, list] = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        original = self.containers[index]
        if original == number:
            return
        self.containers[index] = number
        new_indicies = self.indices_map[number]
        insort(new_indicies, index)
        if original != 0:
            self.indices_map[original].remove(index)

    def find(self, number: int) -> int:
        if indicies := self.indices_map[number]:
            return indicies[0]
        return -1


class NumberContainersHeap:
    __slots__ = ("containers", "indices_map")

    def __init__(self) -> None:
        self.containers: dict[int, int] = defaultdict(int)
        self.indices_map: dict[int, list] = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.containers[index] == number:
            return
        self.containers[index] = number
        new_indicies = self.indices_map[number]
        heappush(new_indicies, index)

    def find(self, number: int) -> int:
        indicies = self.indices_map[number]
        while indicies:
            ans = indicies[0]
            if self.containers[ans] == number:
                return ans
            heappop(indicies)
        return -1
