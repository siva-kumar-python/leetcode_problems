class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ans = []
        for i in range(len(nums)):
            if nums[i]==1:
                ans.append(i)

        for i in range(len(ans)-1):
            if abs(ans[i]-ans[i+1])<k+1:
                return False
            
                
        return True