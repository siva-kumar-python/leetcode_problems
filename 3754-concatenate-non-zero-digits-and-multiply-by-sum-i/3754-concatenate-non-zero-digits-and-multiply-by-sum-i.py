class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        x=str(n).replace('0','')
        ans=0
        for i in x:
            ans+=int(i)
        return int(x)*ans