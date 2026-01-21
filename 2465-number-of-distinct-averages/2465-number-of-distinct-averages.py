class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen=set()
        l,r=0,len(nums)-1
        while l<r:
            temp=(nums[l]+nums[r])/2
            seen.add(temp)
            l+=1
            r-=1
        return len(seen)