class Solution:
    def residuePrefixes(self, s: str) -> int:
        count=0
        seen = set()
        prefix=''
        for i in s:
            prefix+=i
            mod=len(prefix)%3
            if i not in seen :
                seen.add(i)
            if mod==len(seen) and len(seen):
                count+=1
        return count
            
            
