#1046. Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)-1):
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]    