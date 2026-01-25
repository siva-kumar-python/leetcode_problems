class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,k-1
        ans=[]
        while r<len(nums):
            ans.append(nums[r]-nums[l])
            r+=1
            l+=1
        return min(ans) if len(ans) else 0