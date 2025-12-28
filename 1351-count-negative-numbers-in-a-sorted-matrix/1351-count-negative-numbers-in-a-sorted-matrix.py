class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def check(l):
            n=len(l)
            for i in range(n):
                if l[i]<0:
                    return n-i
            return 0
        
        count=0
        for i in grid:
            count+=check(i)
        return count

