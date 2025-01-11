from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        arr = [0] * 26
        for ch in s:
            idx = ord(ch) - 97
            arr[idx] += 1
        pairs = 0
        singles = 0
        for count in arr:
            if count > 0:
                q, r = divmod(count, 2)
                pairs += q
                singles += r

        if singles > k:
            return False
        if singles == k:
            return True
        if singles + pairs >= k:
            return True
        remaining = k - singles - pairs
        return remaining <= pairs

    def canConstruct2(self, s: str, k: int) -> bool:
        """With a check that len(s) > k, we don't need to check the number of pairs anymore."""
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        return sum(count & 1 for count in Counter(s).values()) <= k
