class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans=[]
        for i in range(len(strs[0])):
            res=[]
            for j in range(len(strs)):
                res.append(strs[j][i])
            ans.append(res)
        count=0
        for i in ans:
            if sorted(i)!=i:
                count+=1
        return count
                