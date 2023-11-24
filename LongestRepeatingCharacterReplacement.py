class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        starts = []
        for i in range(n):
            if not starts or s[i] != starts[-1]:
                starts.append(i)

        for i in range(n):
            if s[i] == starts[0]:
                letter = starts.pop(0)


        return res
