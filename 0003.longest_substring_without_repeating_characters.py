from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        queue = deque()
        contents = set()
        for ch in s:
            if ch in contents:
                ans = max(ans, len(contents))
                while (popped := queue.popleft()) != ch:
                    contents.remove(popped)
            queue.append(ch)
            contents.add(ch)

        return max(ans, len(contents))
