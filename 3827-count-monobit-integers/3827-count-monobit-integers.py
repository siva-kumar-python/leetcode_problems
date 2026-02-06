class Solution:
    def countMonobit(self, n: int) -> int:
        if n==0:
            return 1
        
        count=1
        temp=0
        for i in range(11):
            temp+=pow(2,i)
            if temp in range(n+1):
                count+=1
            if temp>n:
                return count
        return count
