class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def check(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        count=0
        for i in range(left,right+1):
            
            if check(bin(i)[2:].count('1')):
                count+=1
        return count