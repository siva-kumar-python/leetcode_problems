class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
            suffix.append(suffix[-1]+nums[-(i+1)])

        suffix =suffix [::-1]
        for i in range(len(nums)):
            if suffix[i]==prefix[i]:
                return i
        return -1