class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        if '6' in s:
            n=s.index('6')
            s=s[:n]+'9'+s[n+1:]
            return int(s)
                
        return int(s)
                