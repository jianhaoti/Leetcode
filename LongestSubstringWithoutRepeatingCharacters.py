class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = {} #flip s
        n = len(s)
        res = 0
        start = 0

        for i in range(0, n):
            if s[i] in myDict and myDict[s[i]] >= start:
                res = max(res, i - start)
                start = myDict[s[i]]+1
            myDict[s[i]] = i

        res = max(res, n - start)

        return res

