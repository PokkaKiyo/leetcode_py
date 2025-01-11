class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        it = iter(reversed([ch for ch in s if ch in VOWELS]))
        return "".join([ch if (ch not in VOWELS) else next(it) for ch in s])


class Solution2:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        left_chars = []
        right_chars = []

        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] not in VOWELS:
                left_chars.append(s[left])
                left += 1
                continue
            if s[right] not in VOWELS:
                right_chars.append(s[right])
                right -= 1
                continue
            if left == right:
                left_chars.append(s[right])
                break
            left_chars.append(s[right])
            right_chars.append(s[left])
            right -= 1
            left += 1

        return "".join(left_chars) + "".join(reversed(right_chars))
