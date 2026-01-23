class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items=sorted(items1+items2)
        ans=[[0,0]]
        for i,j in items:
            if ans[-1][0]==i:
                ans[-1][1]+=j

            else:
                ans.append([i,j])
        return ans[1:]
       
        