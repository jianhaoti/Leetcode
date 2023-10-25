class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # row n has 2^(n-1) elements, so don't build the thing
        # only k matters, think of n = infinity by monotonicity
        # 0 1 1|0|  1001 100|1|0110
        # find posts (0-indexing): 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8
        # just need to count parity of k ----> 0

        # EX:
        # suppose k = k_0 = 11, and closest start is 2^3 = 8, so distance 3.
        # then, replace this with k_1 = 3
        # nearest post is 2^1 = 2, so distance is 1
        # then replace this with k_2 = 1
        # nearest post is 2^0 = 1, so distance is 0
        # then replace this with k_3 = 0
        # stop condition is when you hit 0, then check parity of i in k_i

        parity = True
        while k > 1:
            parity = not parity
            k = k - self.nearestPost(k)+1
            #print("New k value is " + str(k))


        if parity:
            return 0
        else:
            return 1

    def nearestPost(self, k: int) -> int:
        n = -k
        count = 0
        #print("k = " +str(k))
        while n + pow(2, count)+1 <= 0: # EX: if k = 3, then return 2^1 = 2
            #print("Post at index: " + str(pow(2,count)+1))
            #print("Distance from k: " + str(n+pow(2,count)+1))
            count += 1
        count-=1 #overcounted in while loop by one

        print("The nearest post for k = " + str(k) + " is at index: "+ str(pow(2,count)+1))
        return pow(2, count)+1

#I ran this code once and I got ~top 20%. I ran it exactly the same again I got ~top 80%.
#So don't trust the runtime so much. Either way, this is a O(log k) solution.