class Solution(object):
    def trap(self, height):
        rainwater = 0
        n = len(height)

        # Find the rightmost instance of maxHeight
        maxHeightIndex = 0
        for i in range(0, n):
            if height[i] >= height[maxHeightIndex]:
                maxHeightIndex = i

        left = 0
        right = left + 1

        while right <= maxHeightIndex:
            if height[right] >= height[left]:
                rainwater += self.localWater(height, left, right)
                left = right
                right = left + 1
            else:
                right += 1

        right = n - 1
        left = right - 1

        while left >= maxHeightIndex:
            if height[right] <= height[left]:
                rainwater += self.localWater(height, left, right)
                right = left
                left = right - 1
            else:
                left -= 1

        return rainwater

    def localWater(self, arr, L, R):
        if abs(R - L) == 1:
            return 0
        else:
            totalStones = 0
            height = min(arr[L], arr[R])
            width = R - L - 1
            L += 1
            while L < R:
                totalStones += arr[L]
                L += 1

            return abs(height * width - totalStones)
