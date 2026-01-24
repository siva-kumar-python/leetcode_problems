class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        max_elm=0
        while l<r:
            ans=nums[l]+nums[r]
            if ans>max_elm:
                max_elm=ans
            l+=1
            r-=1
        return max_elm