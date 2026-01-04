class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find_divs(n):
            if n<3:
                return []
            divs=[]
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    divs.append(i)
            return divs
        res=0
        for i in nums:
            ans=find_divs(i)
            if len(ans)==1 and i//ans[0] not in ans:
                res+=(ans[0]+1+i+(i//ans[0])) 
        return res


        