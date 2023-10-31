class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) - 1

        left, right = 0, n

        while right-left > 1:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid

        return min(nums[left], nums[right])

        