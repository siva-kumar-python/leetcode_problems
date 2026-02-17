class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        # keys=[]
        # for i in nums:
        #     if i not in keys:
        #         keys.append(i)
        # values=[]
        # for i in keys:
        #     values.append(nums.count(i))
        # for i in range(len(keys)):
        #     if values.count(values[i])==1:
        #         return keys[i]
        # return -1
        di={}
        for i in nums:
            if i not in di.keys():
                di[i]=1
            else:
                di[i]+=1
        count={}
        for i in di.values():
            if i not in count.keys():
                count[i]=1
            else:
                count[i]+=1
        
        for i in nums:
            if count[di[i]]==1:
                return i
        
        return -1