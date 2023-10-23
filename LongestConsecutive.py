class Solution(object):
    def longestConsecutive(nums: list[int]) -> int:
        setNums = set(nums)
        longestLength = 0

        for element in setNums:
            if element-1 not in setNums:
                tempLength=1
                while (element+tempLength) in setNums:
                    tempLength+=1
                longestLength = max(tempLength, longestLength)
        return longestLength
