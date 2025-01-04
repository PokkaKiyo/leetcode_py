class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        memo: dict[str, list[int]] = {}
        for idx, ch in enumerate(s):
            L = memo.get(ch)
            if L is None:
                memo[ch] = [idx, idx]
            else:
                L[1] = idx
        ans = 0
        for value in memo.values():
            ans += len(set(s[value[0] + 1 : value[1]]))
        return ans

    def countPalindromicSubsequence2(self, s: str) -> int:
        memo = {}
        m = memoryview(s.encode("utf-8"))
        for idx, ch in enumerate(m):
            L = memo.get(ch)
            if L is None:
                memo[ch] = [idx, idx]
            else:
                L[1] = idx
        ans = 0
        for value in memo.values():
            ans += len(set(m[value[0] + 1 : value[1]]))
        return ans
