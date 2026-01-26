class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) == 1:
            return prices
        def check(n,i):
            for i in range(i+1,len(prices)):
                if prices[i]<=n:
                    return prices[i]
            return 0




        min_list = []
        for i in range(len(prices)):
            prices[i]-=check(prices[i],i)
        return prices
        

