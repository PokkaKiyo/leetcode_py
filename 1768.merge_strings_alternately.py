class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        ans: list[str] = []
        while ptr1 < len(word1) and ptr2 < len(word2):
            ans.append(word1[ptr1])
            ans.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        while ptr1 < len(word1):
            ans.append(word1[ptr1])
            ptr1 += 1
        while ptr2 < len(word2):
            ans.append(word2[ptr2])
            ptr2 += 1
        return "".join(ans)


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest

        ans = []
        for pair in zip_longest(word1, word2, fillvalue=""):
            ans.extend(pair)
        return "".join(ans)
