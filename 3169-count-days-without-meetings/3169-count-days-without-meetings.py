class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # ans=[True]*days
        # for i in meetings:
        #     for j in range(i[0],i[1]+1):
        #         ans[j-1]=False
        # return sum(ans)
        p=sorted(meetings)
        ans=[p[0]]
        for i in range(1,len(meetings)):
            if p[i][0] in range(ans[-1][0],ans[-1][-1]+1):
                ans[-1][-1]=max(ans[-1][-1],p[i][-1])
            else:
                ans.append(p[i])
                
        for i in ans:
            days-=i[-1]-i[0]+1
        return days


