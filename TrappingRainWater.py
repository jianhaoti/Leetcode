class Solution(object):
    def trap(self, height):
        #I'm keeping this for learnings sake, but I have a v2. This algoirthm is slow
        #since it's O(nh) where n is size of input array and h is max height
        #this speed is based on a "horizontal then vertical" idea as in tetris
        #the faster algorithm will go from "pole ot pole" and will be O(n)
        
        #### #### ####
        #the idea is "tetris". work from bottom to top
        #at each level, from leftmost nonzero to rightmost nonzero, count number of zeros
        #add number of zeros to total rainwater
        #then subract one from all nonzero elements to go up in level
        #stop when list is all zeros

        #### #### #### ####
        rainwater = 0
        left = 0
        right = len(height)-1
        #level = 1 #testing

        while any(x!=0 for x in height):

            #find the outermost nonzero indices
            while height[left] == 0:
                left+=1

            while height[right] == 0:
                right-=1

            #if indices are not aligned, we're finished with the problem
            if left>=right:
                break

            #print("level: " + str(level)) #testing
            #level+=1 #testing
            #print("left index: " + str(left)) #testing
            #print("right index: " + str(right)) #testing

            for x in range(left, right+1):
                if height[x] == 0:
                    rainwater+=1
                else:
                    height[x]-=1

            #print("total rainwater at: " + str(rainwater)) #testing
        return rainwater

        """
        :type height: List[int]
        :rtype: int
        """
