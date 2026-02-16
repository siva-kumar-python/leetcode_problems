class Solution:
    def reverseBits(self, n: int) -> int:
        # ans=''
        # for i in str(n):
        #     ans+=i
        # rlans=0
        # count=0
        # for i in range(-1,-len(ans),-1):
        #     rlans+=int(ans[i])*pow(2,count)
        #     count+=1
        # return rlans
        b=bin(n)[2:].zfill(32)
        
        ans=0
        for i in range(len(b)):
            ans+=int(b[i])*(2**i)
        return ans
