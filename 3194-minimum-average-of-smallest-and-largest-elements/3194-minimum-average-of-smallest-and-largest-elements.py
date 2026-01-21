class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans=[]
        for i in range(len(nums)//2):
            ans.append((nums[i]+nums[-(i+1)])/2)
        return min(ans)