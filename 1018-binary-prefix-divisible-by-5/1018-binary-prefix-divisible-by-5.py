class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums=str(nums)
        res=''
        for i in nums:
            if i.isalnum():
                res+=i
        
        ans=[]
        for i in range(1,len(res)+1):
            if int(res[:i],2)%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans