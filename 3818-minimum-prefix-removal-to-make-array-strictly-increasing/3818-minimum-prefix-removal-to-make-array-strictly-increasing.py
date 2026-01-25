class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n=len(nums)
        count=1
        l=n-1
        while l>0:
            if nums[l]>nums[l-1]:
                count+=1
            else:
                break
            l-=1

        return n-count
