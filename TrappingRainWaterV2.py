class Solution(object):
    def trap(self, height):
        rainwater = 0
        n = len(height)

        #### #### ####

        start = 0
        end = n-1

        #keep track of rightMost instance of maxHeight
        maxHeightIndex = 0
        for i in range(0, n):
            if height[i]>= height[maxHeightIndex]:
                maxHeightIndex = i

        #### #### ####
        left = start
        print("Start at: " + str(left))
        right = left + 1

        while right <= maxHeightIndex: #transverse left to right
            if height[right]>= height[left]: #found a right guy as big as left
                rainwater += self.localWater(height, left, right)
                print("Collected Rainwter: "+str(self.localWater(height,left,right)))
                print("End at: " + str(right))
                left = right
                right = left + 1
                print("New starting index: " + str(left))
            else: #otherwise, keep looking
                right += 1
        print("Total rainwater L to R is: " + str(rainwater))

        #### #### ####

        right = end
        print("Start at: " + str(right))
        left = right - 1

        while left >= maxHeightIndex: #transverse right to left
            if height[right]<= height[left]: #found a left guy as big as right
                rainwater += self.localWater(height, left, right)
                #print("Collected Rainwter: "+str(self.localWater(height,left,right)))
                #print("End at: " + str(left))
                right = left
                left = right - 1
                print("New starting index: " + str(right))
            else: #otherwise, keep looking
                left -= 1
        return rainwater

    def localWater(self, arr, L, R):
        if abs(R-L) == 1: #if side by side, return 0
            return 0
        else: #otherwise, there's a gap, and find number of stones between the two
            totalStones = 0
            height = min(arr[L],arr[R])
            width = R-L-1
            L+=1
            while L < R:
                totalStones += arr[L]
                L+=1

            return abs(height*width - totalStones) #local rainwater collected

        