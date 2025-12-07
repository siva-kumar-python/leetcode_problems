class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=(high-low)//2
        if low%2==1:
            return ans+1
        return ans if high%2==0 else ans+1
       
        