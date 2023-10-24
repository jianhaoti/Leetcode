class Solution(object):
    def trap(self, height):
        rainwater = 0
        n=len(height)
        #### #### ####
        left = 0 #find first nonzero instance
        while left==0:
            left+=1
        leftHeight = height[left]

        end = n-1 #find last nonzero instance
        while end==0:
            end-=1

        hashMap = {}
        for x in range (left, end+1):
            hashMap.update({height[x]}) #value keeps track of rightmost? appearance

        while left < end-1:
            totalStones = 0
            right = left+1
            rightHeight = height[right]

            while rightHeight <= leftHeight: #find the next guy who is as tall
                totalStones+=rightHeight
                right+=1

            if right == : #if one doens't exist, then reset. this part might be slow. keep track with a hashmap?


            rainwater+= ((right-left-1)*leftHeight)-totalStones
            left = right
        return rainwater