class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len(piles)==3:
            return piles[1]
        n=len(piles)//3
        
        l=len(piles)-2
        coins=0
        while n :
            coins+=piles[l]
            n-=1
            l-=2
        return coins