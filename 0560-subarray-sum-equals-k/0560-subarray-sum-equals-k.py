class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={}
        count=0
        prefix=0
        for i in nums:
            prefix+=i

            if prefix==k:
                count+=1
            if prefix-k in seen:
                count+=seen[prefix-k]
            if prefix not in seen.keys():
                seen[prefix]=1
            else:
                seen[prefix]+=1

        return count
        