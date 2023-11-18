class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # you have A/B/...Z-blobs of certain lengths, and certain distances from each other
        # k allows you the amount of leverage you can use to connect certain blobs together.
        # maximize over all blobs by using sliding window for each *-blob?
        # i think this is O(n)

        letters = {}
        for i in range(n):  # finds all places lettes occur
            if s[i] not in letters:
                letters.add(s[i])
                letters[s[i]] = {}
            letters[s[i]].append(i)

        starts = {}
        for letter in letters: # finds start of each blob
            for index in letters[letter]
                if index - 1 not in letters[letter]
                    if letter not in starts:
                        starts[letter] = set()
                    starts[letter].add(i)

        res = 0
        for letter in letters:
            for index in range(len(letters[letter])):
                if letters[letter][index] in starts[letter]:
                    gaps = 0 #
                    i = 1
                    while gaps <= k:
                        gaps = gaps + index+i
                        i = i+1



        return res
