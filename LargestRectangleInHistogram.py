class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        areas = [0] * n
        tempStack = []

        for ind in range(0, n):
            count = 0
            while tempStack and heights[ind] < heights[tempStack[-1][0]]:
                areas[tempStack[-1][0]] = (ind - tempStack[-1][0] + tempStack[-1][1]) * heights[tempStack[-1][0]]
                tempStack.pop()
                count +=1
            tempStack.append((ind, count))

        print(tempStack)

        #left with monotonically increasing tempStack - record their areas
        bound = self.findBoundaries(heights)

        left = 0
        while left != len(bound) - 1:
            for i in range(bound[left], bound[left+1]):
                ind = tempStack[i]
                if i == 0:
                    areas[ind[0]] = (bound[left+1]-bound[left]) * heights[ind[0]] # smallest overall in component
                else:
                    areas[ind[0]] = (n - ind[0]) * heights[ind[0]]
            left += 1

        return max(areas)

    def findBoundaries(self, nums) -> List[int]:
        res = []
        n = len(nums)
        if nums[0]!= 0:
            res.append(0)

        for i in range(1, n-1):
            if nums[i] != 0 and (nums[i-1]==0 or nums[i+1]==0):
                res.append(i)

        if nums[n-1]!=0:
            res.append(n-1)

        return res