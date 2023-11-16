class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        else:
            buy = prices[0]
            ret = max(prices[1]-prices[0], 0)
            for i in range(1,n):
                if buy > prices[i-1]:
                    buy = prices[i-1]
                ret = max(ret, prices[i]-buy)
            return ret