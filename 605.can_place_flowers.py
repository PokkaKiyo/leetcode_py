class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        def left_ok(i) -> bool:
            if i == 0:
                return True
            return flowerbed[i - 1] == 0

        def right_ok(i) -> bool:
            if i == len(flowerbed) - 1:
                return True
            return flowerbed[i + 1] == 0

        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if left_ok(i) and right_ok(i):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
