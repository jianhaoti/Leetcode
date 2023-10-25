#1-indexing used!
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        parity = True
        while k > 1:
            parity = not parity
            k = k - self.nearestPost(k)+1

        if parity:
            return 0
        else:
            return 1

    def nearestPost(self, k: int) -> int:
        n = -k
        count = 0
        while n + pow(2, count)+1 <= 0: #finding the correct post corresponding to k
            count += 1
        count-=1 # overcounted in while loop by one

        return pow(2, count)+1
