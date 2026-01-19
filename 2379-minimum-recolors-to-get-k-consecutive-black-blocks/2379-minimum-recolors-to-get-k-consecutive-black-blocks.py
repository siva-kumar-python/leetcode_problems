class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if "B"*k in blocks:
            return 0
        ans=[]
        l,r=0,k
        w=blocks[:k].count('W')
        ans.append(w)
        while r<=len(blocks):
            ans.append(blocks[l:r].count('W'))
           
            l+=1
            r+=1
        return min(ans) 