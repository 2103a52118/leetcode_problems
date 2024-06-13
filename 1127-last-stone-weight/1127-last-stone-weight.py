class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)
            if m1 != m2:
                stones.append(m1 - m2)
        return stones[0] if stones else 0