class Solution:
    def clearDigits(self, s: str) -> str:
        chars = []
        clear = 0
        for ch in reversed(s):
            if ch.isdigit():
                clear += 1
                continue
            else:
                if clear > 0:
                    clear -= 1
                    continue
                chars.append(ch)
        return "".join(reversed(chars))
