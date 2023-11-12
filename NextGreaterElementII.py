class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # preprocess of putting the max at the end
        n = len(nums)
        maxIndex = nums.index(max(nums))
        permuteBy = (n-1) - maxIndex
        nums = nums[-permuteBy:] + nums[:-permuteBy] # rotate right by permuteBy

        # run MS on rotated array
        res = [-1] * len(nums)
        tempStack = []

        for i in range(0, n):
            while tempStack and nums[i] > tempStack[-1][0]:
                res[tempStack[-1][1]] = nums[i]
                tempStack.pop()
            tempStack.append((nums[i], i))

        return res[permuteBy:] + res[:permuteBy] # rotate left by permuteBy
