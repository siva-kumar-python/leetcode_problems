class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        # fst,lst=points[0][0],points[-1][0]
        # count=0
        # for i,_ in range(len(points)):
        #     if  i not in (fst,lst):
        #         count+=1
        # return count
        x=[ i for i,j in points]
        ans=[0]
        for i  in range(len(x)-1):
            ans.append(x[i+1]-x[i])
        return max(ans)