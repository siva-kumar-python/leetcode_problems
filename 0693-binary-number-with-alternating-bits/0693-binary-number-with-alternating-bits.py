class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)[2:]
        for i in range(len(b)):
            if i%2==0 and b[i]=='0':
                return False
            elif i%2==1 and b[i]=='1':
                return False
        return True