class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p=0
        n=len(nums)
        while p<n-1:
            if nums[p]==nums[p+1]:
                return False
            if nums[p]<nums[p+1]:
                p+=1
            else:
                break 
        nums=nums[p:]
        if len(nums)==n or len(nums)==1:
            return False
        
        q=0
        n=len(nums)
        while q<n-1:
            if nums[q]==nums[q+1]:
                return False
            if nums[q]>nums[q+1]:
                q+=1
            else:
                break
        nums=nums[q:]
        if  len(nums)==n or len(nums)==1:
            return False
        q=0
        while q<len(nums)-1:
            if nums[q]==nums[q+1]:
                return False
            if nums[q]<nums[q+1]:
                q+=1
            else:
                return False
        return True
        

        
        
            

