class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1=0
        p2=0
        isactive=True
        for i in range(len(nums)):
            if (i+1)%6==0:
                isactive=not isactive
            if nums[i]%2==1:
                isactive = not isactive
            if isactive:
                p1+=nums[i]
            else:
                p2+=nums[i]
        return p1-p2
        