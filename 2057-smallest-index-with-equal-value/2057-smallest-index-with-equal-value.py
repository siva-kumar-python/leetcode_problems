class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans=float('inf')
        for i in range(len(nums)):
            if i%10==nums[i] and i<ans:
                ans =i
        return -1 if ans==float('inf') else ans