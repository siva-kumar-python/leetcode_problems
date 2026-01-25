class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i,j in enumerate(nums):
            if j>-1:
                di[i]=j
        ans=list(di.values())
        if len(ans)==0:
            return nums
        n=k%len(ans)
        ans=ans[n:]+ans[:n]
        
        count=0
        for i,j in di.items():
            nums[i]=ans[count]
            count+=1
        return nums
        