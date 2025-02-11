class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) == 1:
            front, last_ch = None, part
        else:
            front, last_ch = list(part[:-1]), part[-1]

        stack = []
        for ch in s:
            if ch != last_ch:
                stack.append(ch)
                continue
            if front is None:
                continue
            if stack[-len(front) :] == front:
                stack = stack[: -len(front)]
            else:
                stack.append(ch)

        return "".join(stack)

    def removeOccurrences_trivial(self, s: str, part: str) -> str:
        while True:
            left, _, right = s.partition(part)
            if not right:
                return left
            s = left + right
