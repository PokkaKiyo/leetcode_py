from math import gcd, sqrt


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for divisor in reversed(find_divisors(len(str1), len(str2))):
            divisor_str = str1[:divisor]
            if (
                str1 == (divisor_str * (len(str1) // divisor))
                and (divisor_str * (len(str2) // divisor)) == str2
            ):
                return divisor_str
        return ""


def find_divisors(n: int, m: int) -> list[int]:
    gcd_ = gcd(n, m)
    divisors: list[int] = []
    for i in range(1, int(sqrt(gcd_))):
        if gcd_ % i == 0:
            divisors.append(i)
    divisors.append(gcd_)
    return divisors
