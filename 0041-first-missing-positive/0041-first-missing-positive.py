class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans=set(nums)
        i=1
        while i in ans:
            i+=1
        return i