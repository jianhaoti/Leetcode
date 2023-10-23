class Solution(object):
    def maxArea(self, height):
        n = len(height)
        maxArea = 0
        left = 0
        right = n-1

        while left < right:
            area = (right-left)*min(height[right], height[left])
            if area > maxArea:
                maxArea = area
            if height[left] < height[right]:
                left+=1
            elif height[left] > height[right]:
                right-=1
            else:
                left+=1
                right-=1
        return maxArea
