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
        for i in range(0, len(tempStack)):
            ind = tempStack[i]
            if i == 0:
                areas[ind[0]] = n * heights[ind[0]] #smallest overall
            else:
                areas[ind[0]] = (n - ind[0]) * heights[ind[0]]
        print(areas)
        return max(areas)