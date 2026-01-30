class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums=nums[::-1]
        ans=set()
        for i in range(len(nums)):
            if nums[i] in range(k+1):
                ans.add(nums[i])
            if len(ans)==k:
                return i+1
        
        