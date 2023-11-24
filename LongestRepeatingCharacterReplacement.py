class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        starts = []
        for i in range(n):
            if not starts or s[i] != starts[-1]:
                starts.append(i)

        maxWindow = 1
        same = 0
        for i in range(n): # just move the window, don't destroy s. destroying is incompatible with starts
            if s[i] == starts[0]:
                letter = starts.pop(0)

                if n - i >= maxWindow: # if i can fit a window
                    change = s[0,maxWindow].count(letter)
                    nonOccurences = maxWindow - occurences
                    change = k -  nonOccurences

                    while change >= 0:
                        if



        return maxWindow
