class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        di={0:[0]}
        m1=0
        for i in range(len(mat)):
            c=mat[i].count(1)
            if c not in di.keys():
                di[c]=[i]
            else:
                di[c].append(i)
            if c>m1:
                m1=c
        return [di[m1][0],m1]
        
