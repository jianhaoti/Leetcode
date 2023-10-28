class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        return self.bSearch(nums, left, right, target)

    def bSearch(self, nums, left, right, target) -> int:
        if left <= right:
            middle = (left + right)//2
            if nums[middle] > target:
                return self.bSearch(nums, left, middle-1, target)
            elif nums[middle] < target:
                return self.bSearch(nums, middle+1, right, target)
            else:
                return middle
        else:
            return -1

        