import functools


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        @functools.cache
        def dp(right_ptr: int, remaining: int) -> list[str]:
            ans: list[str] = []
            for i in range(3):
                left_ptr = right_ptr - i
                if left_ptr < 0:
                    break
                value = s[right_ptr - i : right_ptr + 1]
                if value.startswith("0") and i != 0:
                    continue
                if int(value) > 255:
                    break
                if remaining == 1:
                    if left_ptr == 0:
                        ans.append(value)
                    else:
                        continue
                else:
                    candidates: list[str] = dp(left_ptr - 1, remaining - 1)
                    for candidate in candidates:
                        ans.append(f"{candidate}.{value}")

            return ans

        return dp(len(s) - 1, 4)
