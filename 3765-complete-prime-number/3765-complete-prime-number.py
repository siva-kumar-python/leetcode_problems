class Solution:
    def completePrime(self, num: int) -> bool:
        def isprime(s):
            if s==1:
                return False
            for i in range(2,int(s*0.5)+1):
                if s%i==0:
                    return False
            return True
        if num==1:
            return False
        n=str(num)
        for i in range(len(n)):
            prefix=int(n[:i+1])
            suffix=int(n[-(i+1):])
            
            if not isprime(prefix) or (not isprime(suffix))  :
                return False
        return True
