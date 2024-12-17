from collections import Counter
from dataclasses import dataclass
from heapq import heapify, heappop, heappush


class Solution1:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = self._create_max_heap(s)
        ans: list[str] = []
        while max_heap:
            neg_ch_int, freq = heappop(max_heap)
            ch = chr(-neg_ch_int)
            ans.append(ch * min(freq, repeatLimit))
            freq -= min(freq, repeatLimit)

            if freq > 0:
                if max_heap:
                    neg_ch_int2, _ = max_heap[0]
                    ch2 = chr(-neg_ch_int2)
                    ans.append(ch2)
                    max_heap[0][1] -= 1
                    if max_heap[0][1] == 0:
                        heappop(max_heap)
                else:
                    break

            if freq > 0:
                heappush(max_heap, [neg_ch_int, freq])

        return "".join(ans)

    def _create_max_heap(self, s: str) -> list[list[int]]:
        max_heap = [[-ord(ch), count] for ch, count in Counter(s).items()]
        heapify(max_heap)
        return max_heap


# this is probably what I would do in actual code, although it is slower
@dataclass(order=True, slots=True)
class Pair:
    neg_ch_int: int
    count: int

    @classmethod
    def from_ch(cls, ch: str, count: int):
        return cls(-ord(ch), count)

    @property
    def ch(self) -> str:
        return chr(-self.neg_ch_int)


class Solution2:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = self._create_max_heap(s)
        ans: list[str] = []
        while max_heap:
            pair = heappop(max_heap)
            ch = pair.ch
            max_appearances = min(pair.count, repeatLimit)
            ans.append(ch * max_appearances)
            pair.count -= max_appearances

            if pair.count == 0:
                continue

            if pair.count > 0:
                if not max_heap:
                    break
                next_pair = max_heap[0]
                ans.append(next_pair.ch)
                next_pair.count -= 1
                if next_pair.count == 0:
                    heappop(max_heap)
                heappush(max_heap, pair)

        return "".join(ans)

    def _create_max_heap(self, s: str) -> list[Pair]:
        max_heap = [Pair.from_ch(ch, count) for ch, count in Counter(s).items()]
        heapify(max_heap)
        return max_heap
