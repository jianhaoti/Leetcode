class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # it's interesting to contrast this with trapping rain water (TRW)
        # the reason TRW admits a 2 pointer approach and not just a
        # monotonic stack approach is because you can bypass the nesting behavior.
        # but in DT you need to record it, so it doesn't admit a 2 pointer approach.

        n = len(temperatures)
        res = [0] * n
        tempStack = []

        for i in range(0, n):
            while tempStack and temperatures[i] > tempStack[-1][0]:
                index = tempStack[-1][1]
                res[index] = i - index
                tempStack.pop()
            tempStack.append((temperatures[i],i))


        return res

