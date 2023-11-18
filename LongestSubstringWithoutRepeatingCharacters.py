class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = {} #flip s
        n = len(s)
        res = 0

        for i in range(0, n):
            if s[i] in myDict:
                res = max(res, len(myDict))
                myDict = {key:value for key,value in myDict.items() if key > s[i]}
            myDict[s[i]] = i

        res = max(res,len(myDict))

        return res