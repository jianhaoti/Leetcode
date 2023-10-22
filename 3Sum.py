class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(n^2) algorithm
        #first sort.
        #then, define 3 pointers, one "wall" and a left/right pointer wrt the wall. these two pointer go to the wall
        #the stopping condition (which increments the wall by 1) is when one of the left/right
        #pointers hits the wall. now run sorted 2sum on the left/right pointers.
        #if you hit a solution, you in/dec-crement both pointers by 1 simulatenously.
        #this works since you have 3-1=2 degrees of freedom! if the problem was 4sum, we would be
        #forced to make a 2-nary tree here, where left index increments and right index decrements

        nums.sort()

        #initialize as a hashmap to count unique solutions
        solutions = {}
        n = len(nums)
        for wall in range(1,n-1):
            left = 0
            right = n-1
            while left != wall and right != wall:
                sum = nums[left] + nums[right] + nums[wall]
                if sum == 0:
                    found = (nums[left], nums[wall], nums[right])
                    if found not in solutions:
                        solutions.update({found:1})
                    left+=1
                    right-=1
                elif sum > 0:
                    right-=1
                elif sum <0:
                    left+=1

        return list(solutions)


