class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = 0
        n = len(piles)

        for element in piles: #O(n)
            maxValue = max(element, maxValue)

        left, right = 0, maxValue
        print("Search space from", left, "to", right)

        while left < right:
            mid = (left + right)//2
            print("Mid:", mid)
            if self.fastEnough(piles, h, mid):
                right = mid - 1
                print("Search space from", left, "to -", right, "-")
            else:
                left = mid + 1
                print("Search space from -", left, "- to", right)
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

            print("Total time is:", time)
            return time <= h
        return False




