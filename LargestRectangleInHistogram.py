class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        boundaries = self.boundaries(heights) # length at lesat 2
        m = len(boundaries)
        for i in range(0, m-1, 2)
            left = boundaries[i]
            right = boundaries[i+1]
            self.work(left )

        return 0

    def work(self, ) -> int


    def boundaries(self, nums) -> List[int]:
        res = []
        n = len(nums)
        if nums[0]!=0:
            res.append(0)

        for i in range(1, n-1):
            while nums[i] == 0 and nums[i-1]:


        if nums[n-1]!=0:
            res.append(n-1)

        return res


