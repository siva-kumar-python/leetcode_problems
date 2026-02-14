class Solution:
    def reverseByType(self, s: str) -> str:
        char=''
        sp=''
        for i in s:
            if i.isalpha():
                char=i+char
            elif not i.isdigit():
                sp=i+sp
        if len(char)==0 or len(sp)==0:
            return sp if len(char)==0 else char
        
        ans=''
        j,k=0,0
        for i in s:
            if i.isalpha():
                ans+=char[j]
                j+=1
            elif not i.isdigit():
                ans+=sp[k]
                k+=1
        return ans
        