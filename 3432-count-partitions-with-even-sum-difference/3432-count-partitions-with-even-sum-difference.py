class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0 
        for i in range(len(nums)-1):
            if (sum(nums[:i])-sum(nums[i:]))%2==0:
                count+=1
        return count