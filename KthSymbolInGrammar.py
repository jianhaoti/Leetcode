class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # row n has 2^(n-1) elements, so don't build the thing
        # only k matters, think of n = infinity by monotonicity
        # replace k with 0-indexing, so k = k-1

        k = k - 1
        # 0 1 10 1001 100|1|0110
        # find posts (0-indexing): 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8
        # just need to count parity of k ----> 0

        # EXAMPLE:
        # suppose k = k_0 = 11, and closest start is 2^3 = 8, so distance 3.
        # then, replace this with k_1 = 3
        # nearest post is 2^1 = 2, so distance is 1
        # then replace this with k_2 = 1
        # nearest post is 2^0 = 1, so distance is 0
        # then replace this with k_3 = 0
        # stop condition is when you hit 0, then check parity of i in k_i

        parity = True
        while k != 0:
            k = k - self.nearestPost(k)
            parity = not parity

        if parity:
            return 0
        else:
            return 1

    def nearestPost(self, k: int) -> int:
        n = -k
        count = 0
        while n + pow(2, count) < 0: # if k = 3, return 2^1 = 2
            count += 1
        return pow(2, count)
