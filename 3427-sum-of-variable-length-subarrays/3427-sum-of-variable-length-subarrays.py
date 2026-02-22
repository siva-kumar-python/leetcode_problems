class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        ans=prefix[0]
        for i in range(1,len(nums)):
            start=max(0,i-nums[i])
            if start==0:
                res=prefix[i]
            else:

                res=prefix[i]-prefix[start-1]
            ans+=res
        return ans


        