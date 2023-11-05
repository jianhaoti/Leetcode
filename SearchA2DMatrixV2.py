class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = 0
        n = len(piles)

        for element in piles: #O(n)
            maxValue = max(element, maxValue)

        left, right = 0, maxValue
        while left < right:
            mid = (left + right)//2
            if self.fastEnough(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1
        if self.fastEnough(piles, h, right):
            return right
        return right+1

    def fastEnough(self, piles: List[int], h:int, k:int) -> bool:
        time = 0
        if k != 0:
            for element in piles:
                if element%k != 0:
                    element = element - element%k + k
                time += element/k

            return time <= h
        return False




