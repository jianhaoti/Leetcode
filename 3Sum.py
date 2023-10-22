class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #hard to beat O(n^2) since three equations
        #and 1 constraint => 2 degrees of freedom.

        #howver, we can push this to nlogn
        #the idea is to sort: O(nlogn)
        #then use 2 pointer method on sorted 2sum + varying pointer with binary search

        #### #### ####
        nums.sort()
        n = len(nums)
        solutions = []
        pointerLeft = 0
        pointerRight = n-1

        while pointerLeft < pointerRight:
            answer = self.bSearch(nums, pointerLeft, pointerRight, 0 - nums[pointerLeft] - nums[pointerRight])
            pointerLeft+=1
            pointerRight-=1
            if answer is not None:
                solutions.append([nums[pointerLeft], nums[pointerRight], nums[answer]])

        return solutions

    ##left and right are pointers, seek is an desired element in arr
    def bSearch(self, arr: List[int], left: int, right:int, seek:int) -> int:
        midpoint = left+right//2

        if right-left>=2:
            if seek == arr[midpoint]:
                return seek
            elif seek > arr[midpoint]:
                self.bSearch(arr, midpoint, right, seek)
            elif seek < arr[midpoint]:
                self.bSearch(arr, left, midpoint, seek)

        #if no solution
        return None