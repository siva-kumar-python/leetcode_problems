class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n==len(original):

            ans=[]
            count=0
            for i in range(m) :
                res=[]
                for j in range(n):
                    res.append(original[count])
                    count+=1

                ans.append(res)
            return ans
        return []