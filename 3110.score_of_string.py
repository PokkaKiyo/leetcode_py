from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        last = ord(s[0])
        for x, y in pairwise(s):
            ord_y = ord(y)
            ans += abs(last - ord_y)
            last = ord_y
        return ans
