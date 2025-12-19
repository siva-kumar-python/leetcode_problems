class Solution:
    def gcdOfStrings(self, small: str, big: str) -> str:
        if len(set(small))!=len(set(big)):
            return ''
       
        
        for i in range(len(small),0,-1):
            temp=small[:]
            res=big[:]
            temp=temp.replace(big[:i],'')
            res=res.replace(big[:i],'')
            if len(temp)==0 and len(res)==0:
                return big[:i]
            
        return '' 