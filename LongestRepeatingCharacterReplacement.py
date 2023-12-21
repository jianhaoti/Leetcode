class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        starts = [0]
        for i in range(1, n-1):
            letter = s[starts[-1]]
            if s[i]!= letter:
                starts.append(i)
                letter =  s[i]

        if s[n-1] != s[n-2]:
            starts.append(n-1)

        maxWindow = 1
        same = 0
        for i in range(n): # just move the window, don't destroy s. destroying is incompatible with starts
            if s[i] == s[starts[0]]:
                letter = s[starts.pop(0)]

                if n - i >= maxWindow: # can i fit a window?
                    occurences = s[0:maxWindow].count(letter)
                    nonOccurences = maxWindow - occurences
                    change = k -  nonOccurences

                    j = maxWindow
                    while change >= 0 and i+j < n:
                        if s[i+j]!= letter:
                            change -= 1
                        j += 1
                        maxWindow += 1

        return maxWindow
