class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n+1):
            s=str(int('0110',i))
            if s!=s[::-1]:
                return False
        return True