class Solution:
    def removeOccurrences_trivial(self, s: str, part: str) -> str:
        while True:
            left, _, right = s.partition(part)
            if not right:
                return left
            s = left + right
