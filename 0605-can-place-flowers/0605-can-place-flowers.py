class Solution:
    def canPlaceFlowers(self, n: List[int], m: int) -> bool:
        c = 0
        i = 0
        while i < len(n):
            if n[i] == 0 and (i == 0 or n[i-1] == 0) and (i == len(n) - 1 or n[i+1] == 0):
                n[i] = 1
                c += 1
            i += 1
        return c >= m
