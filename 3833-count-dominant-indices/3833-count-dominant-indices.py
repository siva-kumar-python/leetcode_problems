class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans=[]
        tot=sum(nums)
        s=0
        for i in  nums:
            temp=tot-i
            ans.append(temp)
            tot=temp
        count=0
        n=len(nums)
        for i in range(n-1):
            res=ans[i]/(n-(i+1))
            if nums[i]>res:
                count+=1
        return count